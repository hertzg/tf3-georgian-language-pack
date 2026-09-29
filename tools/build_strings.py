# Builds the mod's English + Georgian text: the game's English strings with the
# Georgian overrides from translations/*.json applied on top.
#
#   python3 tools/build_strings.py "<TF3 install>/base/strings/en/LC_MESSAGES/base.mo"
#
# Needs gettext (msgunfmt, msgfmt). Writes
# hertzg_georgian_names/strings/en/LC_MESSAGES/base.mo.
#
# Entries in translations/*.json:
#   {"msgid": "...", "msgstr": "..."}                              plain _()
#   {"msgctxt": "town-level", "msgid": "...", "msgstr": "..."}      pGetText(ctx, ...)
#   {"msgid": "%s Year", "msgid_plural": "%s Years", "msgstr": "%s წელი"}
#                                                                   nGetText; Georgian uses the
#                                                                   same form after any number;
#                                                                   add "msgstr_one" when the singular
#                                                                   msgid has a literal 1 instead
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "hertzg_georgian_names", "strings", "en", "LC_MESSAGES", "base.mo")


def unescape_lua(s):
    # msgids taken from game scripts keep their Lua escapes (\" and \n)
    return re.sub(r'\\(["n\\])', lambda m: {"n": "\n"}.get(m.group(1), m.group(1)), s)


def po_quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def parse_po(text):
    # Minimal PO reader: one dict per entry, keyed by field name
    # (msgctxt, msgid, msgid_plural, msgstr, msgstr[0], ...).
    entries = []
    for block in re.split(r"\n\s*\n", text.strip()):
        entry, field = {}, None
        for line in block.splitlines():
            if line.startswith("#"):
                continue
            m = re.match(r'^(msgctxt|msgid_plural|msgid|msgstr(?:\[\d+\])?) (".*")$', line)
            if m:
                field = m.group(1)
                entry[field] = json.loads(m.group(2))
            elif line.startswith('"') and field:
                entry[field] += json.loads(line)
        if "msgid" in entry:
            entries.append(entry)
    return entries


def write_po(entries):
    out = []
    for e in entries:
        lines = []
        for field in ["msgctxt", "msgid", "msgid_plural"]:
            if field in e:
                lines.append(f"{field} {po_quote(e[field])}")
        for field in sorted(k for k in e if k.startswith("msgstr")):
            lines.append(f"{field} {po_quote(e[field])}")
        out.append("\n".join(lines))
    return "\n\n".join(out) + "\n"


def key(e):
    return (e.get("msgctxt"), e["msgid"])


def main(base_mo):
    overrides = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "translations", "*.json"))):
        for e in json.load(open(path, encoding="utf-8")):
            entry = {"msgid": unescape_lua(e["msgid"])}
            if e.get("msgctxt"):
                entry["msgctxt"] = e["msgctxt"]
            if e.get("msgid_plural"):
                entry["msgid_plural"] = unescape_lua(e["msgid_plural"])
                entry["msgstr[0]"] = entry["msgstr[1]"] = unescape_lua(e["msgstr"])
                if e.get("msgstr_one"):  # singular msgid without the number placeholder
                    entry["msgstr[0]"] = unescape_lua(e["msgstr_one"])
            else:
                entry["msgstr"] = unescape_lua(e["msgstr"])
            overrides[key(entry)] = entry

    with tempfile.TemporaryDirectory() as tmp:
        base_po = os.path.join(tmp, "base.po")
        subprocess.run(["msgunfmt", "--no-wrap", base_mo, "-o", base_po], check=True)
        entries = parse_po(open(base_po, encoding="utf-8").read())

        replaced = 0
        for i, e in enumerate(entries):
            if key(e) in overrides:
                entries[i] = overrides.pop(key(e))
                replaced += 1
        added = len(overrides)
        entries.extend(overrides.values())

        merged_po = os.path.join(tmp, "merged.po")
        open(merged_po, "w", encoding="utf-8").write(write_po(entries))
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        subprocess.run(["msgfmt", "--check-format", merged_po, "-o", OUT], check=True)

    print(f"{replaced} replaced, {added} added -> {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1])
