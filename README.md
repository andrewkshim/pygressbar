# Terminal Progress Bar
Simple module used for Python terminal programs. If your program takes a while
to run and you'd like to observe its progress, you've come to the right place.

# Installation
```bash
pip install pygressbar
```

# Example
```python
import pygressbar

limit = 1000000
progress_bar = pygressbar.ProgressBar(limit)
for i in range(0, limit):
  progress_bar.render()
```
To see this in action, execute [pygressbar\_sample.py](./pygressbar_sample.py).

# License
This content is released under the [MIT License](./LICENSE.md).

# Changes
