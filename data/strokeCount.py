"""
Unihan source: https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip
               https://www.unicode.org/Public/UCD/latest/ucd/
Current version: https://www.unicode.org/reports/tr38/ (2021-08-26)
"""

import json
from pathlib import Path

p = Path('Unihan/Unihan_IRGSources.txt')

strokeCounts = {}
with open(p) as f:
	for l in f:
		l = l.strip()
		if l.startswith('#') or l == '': continue
		# kTotalStrokes
		ch, tp, val = l.split('\t')
		if tp != 'kTotalStrokes': continue
		ch = chr(int(ch.strip()[2:], 16))
		if ' ' in val:
			val = val.strip().split()[-1]
		strokeCounts[ch] = int(val)

with open('strokeCount.json', 'w', encoding='utf-8') as f:
	json.dump(strokeCounts, f, ensure_ascii=False, separators=(',', ':'))
