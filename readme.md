# Various Helpers (Python3) (WIP)

This repo serves as a collection of various functions, classes, & code snippets as they begin to make multiple appearances in multiple projects. Pre-existing repositories for decorators & context managers now live here. This is also a place for smaller modules, bits, & bytes that don't necessarily warrant an entire repo of their own. 

## Contents:
- Context managers
- Common conversions not served by the standard library
- Decorators
- File / path utilities
- Tkinter helper(s)

## Contents in detail:
- ##### Context_Managers:
	- Outfile.py
		- `Outfile()`: Redirect stdout => file.txt
	- Precision.py
		- `Precision()`: Set decimal precision
	- Timer.py
		- `Timer()`: wrapper for time.perf_counter()
- ##### Conversions:
	- color_notation.py
		- `rgb_to_hex()`: (255,255,255) => "#FFFFFF"
		- `hex_to_rgb()`: ("#FFFFFF") => (255,255,255)
- ##### Decorators:
	- Cached.py
		- `cached_single_arg()`: Super-simple memoize (single argument)
	- Counted.py
		- `counted()`: Function call counter => stdout
	- Logged.py
		- `logged()`: Datetime functin logger => stdout
	- Timed.pu
		- `timed()`: wrapper for time.perf_counter() => stdout
	- TimedAverage.py
		- `timed_average()`: (See Timed) Runs a function [iterations] times and returns the result of the last. average time => stdout
- ##### File_Utils:
	- get_disks.py
		- `get_disks()`: Return all mounted disk names as a list of strings (Windows) => ["C:/", "D:/", "E:/"]
	- name_dupe.py
		- `name_dupe()`: Return a filename appended w/ an index to avoid overwrite => file.txt => file(2).txt
- #### Tk_Tools:
	- get_offset.py
		- `get_offset()`: Returns an appropriate offset for a given tkinter toplevel, such that it always shows center screen on the primary display, given its existing dimensions.

## Usage:
### Context_Managers:
(coming soon)

---

### Conversions:

- color_notation.py

	- `rgb_to_hex(rgb)`

	- `hex_to_rgb(hex_)`

```
#app.py

from color_notation import rgb_to_hex, hex_to_rgb

print(rgb_to_hex((255,255,255)))
print(hex_to_rgb("#FFFFFF"))
```

```
>> C:\current\working\directory λ python app.py
>> #FFFFFF
>> 255,255,255
>> C:\current\working\directory λ
```

---

### Decorators:
(coming soon)

---

### File_Utils:

- get_disks.py

`get_disks()`

```
#app.py

from get_disks import get_disks

print(get_disks())
```

```
>> C:\current\working\directory λ python app.py
>> ['A:/', 'B:/', 'C:/', 'D:/']
>> C:\current\working\directory λ
```

---

- name_dupe.py

`name_dupe(path)`

We want to rename a file / directory until it doesn't exist anymore to avoid silently overwriting something. Returns original path if it doesn't already exist.

```
#app.py

from name_dupe import name_dupe

paths = [
	r"C:\path\to\existing_file.txt",
    r"C:\path\to\non_existing_file.txt",
    r"C:\path\to\existing_directory",
    r"C:\path\to\non_existing_directory",
]

for path in paths:
	print(name_dupe(path))

```

```
>> C:\current\working\directory λ python app.py
>> C:\path\to\existing_file (1).txt
>> C:\path\to\non_existing_file.txt
>> C:\path\to\existing_directory (1)
>> C:\path\to\non_existing_directory
>> C:\current\working\directory λ
```

---

### Tk_Tools:
- get_offset.py
	- `get_offset(tk_window)` => `(width_offset, height_offset)`
```
from Tkinter import Tk()

window = Tk()
window.geometry(f"{width}x{height}")
window.update()
(width_offset, height_offset) = get_offset(tk_window)
# Then it's very easy to do this:
window.geometry(f"+{width_offset}+{height_offset}")
```
