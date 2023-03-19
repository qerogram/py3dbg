PyDbg for Python 3 and 64 bits
==============================

This is a fork of Pedram Amini's [PyDbg](http://pedramamini.com/PaiMei/docs/) ([archived copy at OpenRCE](https://github.com/OpenRCE/pydbg)) which changes to make it run with Python 3 and on 64 machines.

Some files from [v-p-b/PyDbg](https://github.com/v-p-b/pydbg) are also used.

This is not entirely finished but most of Python 3 changes are done.
For 64 bits, and the general ideas of the changes are exposed:
- Print pointers with %016x instead of %08x.
- Do not really on default argtypes functions specifications used by ctypes.
- Different registers.

What works is the hooking of functions, and it is tested in the project [Survol](https://github.com/rchateauneu/survol).

An excellent introduction to PyDbg can be found in the book [Gray Hat Python](https://www.nostarch.com/ghpython.htm).
