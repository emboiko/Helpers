# Various Helpers (Python3) (WIP)

This repo serves as a collection of various functions, classes, & code snippets as they begin to make multiple appearances in multiple projects. Pre-existing repositories for decorators & context managers now live here. This is also a place for smaller modules, bits, & bytes that don't necessarily warrant an entire repo of their own. 

## Contents:
- Context managers
- Decorators
- File / path utilities
- Simple socket-based IPC utility class
- Tkinter helpers
- Common conversions not served by the standard library

## Contents in detail:
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
	- Timed.pu
		- `timed()`: wrapper for time.perf_counter() => stdout
	- TimedAverage.py
		- `timed_average`: (See Timed) Runs a function [iterations] times and returns the result of the last. => stdout
- ##### File_Utils:
	- get_disks.py
		- `get_disks()`: Return all mounted disk names as a list of strings (Windows) => ["C:/", "D:/", "E:/"]
	- name_dupe.py
		- `name_dupe()`: Return a filename appended w/ an index to avoid overwrite => file.txt => file(2).txt
- #### IPC:
	- socket_singleton.py
		- `Socket_Singleton()`: Allow one instance of an application to run at a time + gather / send arguments.
- #### Tk_Tools:
	- get_offset.py
		- `get_offset()`: Returns an appropriate offset for a given tkinter toplevel, such that it always shows center screen on the primary display, given its existing dimensions.

## Usage:
### Context_Managers:
(coming soon)
### Conversions:
(coming soon)
### Decorators:
(coming soon)
### File_Utils:
(coming soon)
### IPC:
- socket_singleton.py
	- `get_offset(tk_window)` => `(width_offset, height_offset)`

Say we have an application, app.py, that we want to restrict to a single instance.
```
#app.py

from socket_singleton import Socket_Singleton
Socket_Singleton()
input() #Blocking call to simulate your_business_logic() 
```
The first time app.py is launched:
```
>> C:\current\working\directory λ python app.py
>> 
```
app.py runs (Here, app.py blocks until we satisfy input(). Replace this with your own logic.)

Now, in another shell, if we try:
```
>> C:\current\working\directory λ python app.py
>> C:\current\working\directory λ
```
The interpreter exits immediately and we end up back at the prompt.

---
We can also get access to **arguments** passed from subsequent attempts to run `python app.py` with the `arguments` attribute.
This can be accessed directly, but it's probably more convenient to use the `trace()` method. This allows you to register a callback, which gets called when `arguments` is appended.

`Socket_Singleton.trace(observer, *args, **kwargs)`

```
#app.py
from socket_singleton import Socket_Singleton

def callback(app, *args, **kwargs):
    print(app.arguments)

def main():
    app = Socket_Singleton()
    app.trace(callback)
    input() #Blocking call to simulate your_business_logic() 

if __name__ == "__main__":
    main()
```
At the terminal:
```
>> C:\current\working\directory λ python app.py
>> 
```

In another shell, subsequent attempts to `python app.py` now look like this:
```
>> C:\current\working\directory λ python app.py foo bar baz
>> C:\current\working\directory λ
```
Meanwhile, our output for the original `python app.py` shell looks like this:
```
>> C:\current\working\directory λ python app.py
>> ["foo"]
>> ["foo", "bar"]
>> ["foo", "bar", "baz"]
```

---
If you'd prefer to **disconnect** from the port prematurely, thus releasing the "lock", there's a `close()` method:

```
from socket_singleton import Socket_Singleton

def main():
    app = Socket_Singleton()
    app.close()
    input()

if __name__ == "__main__":
    main()
```
At the terminal:
```
>> C:\current\working\directory λ python app.py
>> Running!
>> 
```
And in a new shell:
```
>> C:\current\working\directory λ python app.py
>> Running!
>> 
```


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