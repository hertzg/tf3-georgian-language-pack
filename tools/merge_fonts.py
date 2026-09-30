# Usage: python3 tools/merge_fonts.py Lato-Regular.ttf NotoSansGeorgian-Regular.ttf \
#   GeorgianNamesSans-Regular.ttf "Georgian Names Sans" Regular [size]  (needs fontTools)
# size scales the Georgian letters relative to Lato's x-height (default 1.0).
# Adds the Georgian glyphs of Noto Sans Georgian to Lato, scaled so the
# x-heights match, and renames the result (Lato's license reserves its name).
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen

lato_path, noto_path, out_path, family, style = sys.argv[1:6]
size = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
lato, noto = TTFont(lato_path), TTFont(noto_path)
k = (lato["OS/2"].sxHeight / lato["head"].unitsPerEm) / (noto["OS/2"].sxHeight / noto["head"].unitsPerEm) \
    * lato["head"].unitsPerEm / noto["head"].unitsPerEm * size

ranges = [(0x10A0, 0x10FF), (0x1C90, 0x1CBF), (0x2D00, 0x2D2F)]
ncmap = noto.getBestCmap()
cps = sorted(cp for cp in ncmap if any(a <= cp <= b for a, b in ranges))

nglyf, nset = noto["glyf"], noto.getGlyphSet()
lglyf, lhmtx = lato["glyf"], lato["hmtx"]
order = list(lato.getGlyphOrder())
added = {}
for cp in cps:
    src = ncmap[cp]
    name = "geo." + src
    if name not in added:
        pen = TTGlyphPen(None)
        nset[src].draw(TransformPen(pen, (k, 0, 0, k, 0, 0)))  # decomposes composites
        g = pen.glyph()
        lglyf[name] = g
        adv, lsb = noto["hmtx"][src]
        g.recalcBounds(lglyf)
        lhmtx[name] = (round(adv * k), g.xMin if hasattr(g, "xMin") else 0)
        order.append(name)
        added[src] = name
    for table in lato["cmap"].tables:
        if table.isUnicode():
            if table.format == 4 and cp > 0xFFFF:
                continue
            table.cmap[cp] = name
lato.setGlyphOrder(order)
lglyf.glyphOrder = order
lato["maxp"].numGlyphs = len(order)
if "post" in lato and lato["post"].formatType == 2.0:
    lato["post"].extraNames = []
    lato["post"].mapping = {}

full = f"{family} {style}" if style != "Regular" else family
ps = f"{family.replace(' ', '')}-{style}"
for rec in lato["name"].names:
    if rec.nameID in (1, 16):
        rec.string = family
    elif rec.nameID == 4:
        rec.string = full
    elif rec.nameID == 6:
        rec.string = ps
    elif rec.nameID == 3:
        rec.string = f"{ps};merged from Lato and Noto Sans Georgian"
    elif rec.nameID == 17:
        rec.string = style
lato.save(out_path)
print(out_path, "added", len(added), "glyphs for", len(cps), "code points, scale", round(k, 3))
