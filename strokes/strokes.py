#%%
import json
from pathlib import Path

fp = Path(__file__).parent / "../data/strokeCount.json"
with open(fp, encoding="utf-8") as f:
    data = json.load(f)


def strokes(chars: str, add=False):
    if len(chars) == 1:
        return data.get(chars, 0)
    if len(chars) > 1:
        counts = ( data.get(c, 0) for c in chars )
        if add: return sum(counts)
        return list(counts)
    if len(chars) == 0: return None
