Hanzi Stroke Count
==================


## Install

```bash
pip install strokes
```


## Usage

```python
from strokes import strokes

>>> strokes('众')
6
>>> strokes('众人')
[6, 2]
>>> strokes('眾人')
[11, 2]
>>> strokes('眾人', add=True)
13
>>> strokes('人-泛称')  # non-chinese characters are given a stroke count of zero
[2, 0, 7, 10]
```


## Data Source

Stroke count data are based on [Unihan_IRGSources.txt](https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip) in [Unihan database](https://www.unicode.org/charts/unihan.html).
