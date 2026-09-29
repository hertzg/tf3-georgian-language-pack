# Looks up a word in the National Parliamentary Library of Georgia's dictionary
# collection (nplg.gov.ge/gwdict), the reference for this mod's Georgian terms.
#
#   python3 tools/ka_dict.py rubber          # English-Georgian (d=1)
#   python3 tools/ka_dict.py მაღარო 0         # all dictionaries
#   python3 tools/ka_dict.py მაღარო 46        # big Georgian-English
#
# The site answers 410 Gone to non-browser user agents, hence the header, and
# 429 when asked too often. Requests from parallel runs are queued through a
# lock file, spaced out, retried on 429, and cached, so several agents can use
# this at once. A lookup that still fails exits non-zero instead of claiming
# the word wasn't found.
import fcntl
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse

STATE = os.path.join(tempfile.gettempdir(), "ka_dict")
MIN_GAP = 2.0  # seconds between requests to the site


def fetch(url):
    os.makedirs(STATE, exist_ok=True)
    cache = os.path.join(STATE, hashlib.sha1(url.encode()).hexdigest() + ".html")
    if os.path.exists(cache):
        return open(cache, encoding="utf-8").read()
    with open(os.path.join(STATE, "lock"), "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        stamp = os.path.join(STATE, "last")
        for attempt in range(6):
            last = os.path.getmtime(stamp) if os.path.exists(stamp) else 0
            wait = MIN_GAP - (time.time() - last)
            if wait > 0:
                time.sleep(wait)
            result = subprocess.run(
                ["curl", "-s", "-L", "--max-time", "30", "-w", "\n%{http_code}", "-A",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
                 "(KHTML, like Gecko) Version/17.0 Safari/605.1.15", url],
                capture_output=True, text=True,
            )
            open(stamp, "w").close()
            page, _, status = result.stdout.rpartition("\n")
            if status == "200":
                open(cache, "w", encoding="utf-8").write(page)
                return page
            time.sleep(5 * 2 ** attempt)  # 429 or network error: back off
        sys.exit(f"dictionary unavailable (last HTTP status {status or 'none'}); try again later")


def lookup(term, dictionary="1"):
    query = urllib.parse.urlencode({
        "a": "srch", "q": term, "d": dictionary,
        "srch[adv]": "all", "srch[by]": "d", "srch[in]": "-1",
    })
    page = fetch("http://www.nplg.gov.ge/gwdict/index.php?" + query)

    def text(s):
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()

    # a single exact match skips the result list and opens the term page
    single = re.search(r'<h1 class="term">(.*?)</h1>\s*<ol class="defnblock">(.*?)</ol>', page, re.S)
    if single:
        dictionary_name = text(re.search(r"<title>.*? - (.*?)</title>", page).group(1))
        senses = [text(d) for d in re.findall(r'<div class="defn">(.*?)</div>', single.group(2), re.S)]
        return "1", [dictionary_name], [(text(single.group(1)), " ◊ ".join(senses))]

    found = re.search(r"Found in dictionaries:\s*<strong>(\d+)</strong>", page)
    dicts = [text(d) for d in re.findall(r'<div class="xu dictlist">(.*?)</div>', page, re.S)]
    pairs = re.findall(r'<dt class="termpreview">(.*?)</dt>\s*<dd class="defnpreview">(.*?)</dd>', page, re.S)
    return (found.group(1) if found else "0"), dicts, [(text(t), text(d)) for t, d in pairs]


if __name__ == "__main__":
    count, dicts, pairs = lookup(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "1")
    print(f"found in {count} dictionaries: {'; '.join(dicts)}")
    for term, definition in pairs:
        print(f"{term} — {definition}")
