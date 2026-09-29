# Builds the mod's English + Georgian text: the game's English strings with the
# Georgian overrides from translations/*.json applied on top.
#
#   python3 tools/build_strings.py "<TF3 install>/base/strings/en/LC_MESSAGES/base.mo"
#
# Needs gettext (msgunfmt, msgfmt). Writes
# hertzg_georgian_names/strings/en/LC_MESSAGES/base.mo.
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
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return '"' + s + '"'


def main(base_mo):
    overrides = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "translations", "*.json"))):
        for e in json.load(open(path, encoding="utf-8")):
            overrides[unescape_lua(e["msgid"])] = unescape_lua(e["msgstr"])

    with tempfile.TemporaryDirectory() as tmp:
        base_po = os.path.join(tmp, "base.po")
        subprocess.run(["msgunfmt", "--no-wrap", base_mo, "-o", base_po], check=True)
        text = open(base_po, encoding="utf-8").read()

        replaced = set()

        def swap(m):
            msgid = "".join(json.loads(line) for line in m.group(1).splitlines())
            if msgid in overrides:
                replaced.add(msgid)
                return "msgid %s\nmsgstr %s\n" % (po_quote(msgid), po_quote(overrides[msgid]))
            return m.group(0)

        text = re.sub(r'^msgid ((?:".*"\n)+)msgstr ((?:".*"\n)+)', swap, text, flags=re.M)
        added = [k for k in overrides if k not in replaced]
        text += "".join("\nmsgid %s\nmsgstr %s\n" % (po_quote(k), po_quote(overrides[k])) for k in added)

        merged_po = os.path.join(tmp, "merged.po")
        open(merged_po, "w", encoding="utf-8").write(text)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        subprocess.run(["msgfmt", "--check-format", merged_po, "-o", OUT], check=True)

    print(f"{len(replaced)} replaced, {len(added)} added -> {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1])
