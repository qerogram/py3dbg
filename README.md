# py3dbg
modified the PyDbg library to support x64 processes, enhancing its capabilities.
Some changes have been made to the code in this repository.(https://github.com/rchateauneu/pydbg)

# Install
```sh
$ pip install py3dbg 
```

# Usage
```python
import py3dbg
import py3dbg.defines

PROCESS_NAME = b"program.exe"

def debug_event_handler(dbg):
    if dbg.dbg.u.Exception.dwFirstChance:
        return py3dbg.defines.DBG_CONTINUE
    else:
        return py3dbg.defines.DBG_EXCEPTION_NOT_HANDLED

def debug_stack(dbg) :
    # dump register values
    context = dbg.dump_context()

    # dump stack
    stack = ""
    address = 0
    memsize = 0x4

    if not py3dbg.process_is_wow64(dbg.pid) :
        address = dbg.context.Rsp
        memsize = 0x8
    else :
        address = dbg.context.Esp


    for i in range(16):
        value = dbg.read_process_memory(address, memsize)
        stack += "{:#08x}: {}\n".format(address, value)
        address += memsize
    
    return py3dbg.defines.DBG_EXCEPTION_NOT_HANDLED


dbg = py3dbg.pydbg()

dbg.load(PROCESS_NAME)
dbg.set_callback(py3dbg.defines.EXCEPTION_ACCESS_VIOLATION, debug_stack)
dbg.attach(dbg.pid)
dbg.run()
```