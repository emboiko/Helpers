# Various Helpers (Python3) (WIP)

This repo serves as a collection of various functions, classes, & code snippets as they begin to make multiple appearances in multiple projects. Pre-existing repositories for decorators & context managers now live here. This is also a place for smaller modules, bits, & bytes that don't necessarily warrant an entire repo of their own. 

### Contents:
---
- Context managers
- Decorators
- File / path utilities
- Simple socket-based IPC utility class
- Tkinter helpers
- Common conversions not served by the standard library

### Contents in detail:
---
- ##### Context_Managers:
	- Outfile.py
		- `class Outfile`: Redirect stdout => file.txt
	- Precision.py
		- `class Precision`: Set decimal precision
	- Timer.py
		- `class Timer`: wrapper for time.perf_counter()
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
		- `logged()`: Datetime logger => stdout
	- Timed
		- `timed()`: wrapper for time.perf_counter() => stdout
	- TimedAverage
		- `timed_average`: (See Timed) Runs a function [iterations] times and returns the result of the last. => stdout
- ##### File_Utils:
	- get_disks.py
		- `get_disks()`: Return all mounted disk names as a list of strings (Windows) => ["C:/", "D:/", "E:/"]
	- name_dupe.py
		- `name_dupe()`: Return a filename appended w/ an index to avoid overwrite => file.txt => file(2).txt
- #### IPC:
	- socket_singleton.py
		- `Socket_Singleton()`: Allow one instance of an application to run at a time.
- #### Tk_Tools:
	- get_offset.py
		- `get_offset()`: Returns an appropriate offset for a given tkinter toplevel, such that it always shows center screen on the primary display, given its existing dimensions.

---
### Usage:
(coming soon)