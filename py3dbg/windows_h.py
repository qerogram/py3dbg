# generated by 'xml2py'

#
# $Id: windows_h.py 194 2007-04-05 15:31:53Z cameron $
#


# flags 'windows.xml -s DEBUG_EVENT -s CONTEXT -s MEMORY_BASIC_INFORMATION -s LDT_ENTRY -s PROCESS_INFORMATION -s STARTUPINFO -s SYSTEM_INFO -s TOKEN_PRIVILEGES -s LUID -s HANDLE -o windows_h.py'

# PEDRAM - line swap ... have to patch in our own __reduce__ definition to each ctype.
from .my_ctypes import *

import sys
is_64bits = sys.maxsize > 2**32
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 4188
class _TOKEN_PRIVILEGES(Structure):
    pass
TOKEN_PRIVILEGES = _TOKEN_PRIVILEGES
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 3774
class _STARTUPINFOA(Structure):
    pass
STARTUPINFOA = _STARTUPINFOA
STARTUPINFO = STARTUPINFOA
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1661
class _LDT_ENTRY(Structure):
    pass
LDT_ENTRY = _LDT_ENTRY
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 4534
class _MEMORY_BASIC_INFORMATION(Structure):
    pass
MEMORY_BASIC_INFORMATION = _MEMORY_BASIC_INFORMATION
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 697
class _DEBUG_EVENT(Structure):
    pass
DEBUG_EVENT = _DEBUG_EVENT
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1563
class _CONTEXT(Structure):
    pass
CONTEXT = _CONTEXT
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 497
class _SYSTEM_INFO(Structure):
    pass
SYSTEM_INFO = _SYSTEM_INFO
HANDLE = c_void_p
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 229
class _PROCESS_INFORMATION(Structure):
    pass
PROCESS_INFORMATION = _PROCESS_INFORMATION
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 394
class _LUID(Structure):
    pass
LUID = _LUID
WORD = c_ushort
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1664
class N10_LDT_ENTRY3DOLLAR_4E(Union):
    pass
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1665
class N10_LDT_ENTRY3DOLLAR_43DOLLAR_5E(Structure):
    pass
BYTE = c_ubyte
N10_LDT_ENTRY3DOLLAR_43DOLLAR_5E._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1665
    ('BaseMid', BYTE),
    ('Flags1', BYTE),
    ('Flags2', BYTE),
    ('BaseHi', BYTE),
]
assert sizeof(N10_LDT_ENTRY3DOLLAR_43DOLLAR_5E) == 4, sizeof(N10_LDT_ENTRY3DOLLAR_43DOLLAR_5E)
assert alignment(N10_LDT_ENTRY3DOLLAR_43DOLLAR_5E) == 1, alignment(N10_LDT_ENTRY3DOLLAR_43DOLLAR_5E)
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1671
class N10_LDT_ENTRY3DOLLAR_43DOLLAR_6E(Structure):
    pass
DWORD = c_ulong
N10_LDT_ENTRY3DOLLAR_43DOLLAR_6E._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1671
    ('BaseMid', DWORD, 8),
    ('Type', DWORD, 5),
    ('Dpl', DWORD, 2),
    ('Pres', DWORD, 1),
    ('LimitHi', DWORD, 4),
    ('Sys', DWORD, 1),
    ('Reserved_0', DWORD, 1),
    ('Default_Big', DWORD, 1),
    ('Granularity', DWORD, 1),
    ('BaseHi', DWORD, 8),
]
assert sizeof(N10_LDT_ENTRY3DOLLAR_43DOLLAR_6E) == 4, sizeof(N10_LDT_ENTRY3DOLLAR_43DOLLAR_6E)
assert alignment(N10_LDT_ENTRY3DOLLAR_43DOLLAR_6E) == 4, alignment(N10_LDT_ENTRY3DOLLAR_43DOLLAR_6E)
N10_LDT_ENTRY3DOLLAR_4E._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1664
    ('Bytes', N10_LDT_ENTRY3DOLLAR_43DOLLAR_5E),
    ('Bits', N10_LDT_ENTRY3DOLLAR_43DOLLAR_6E),
]
assert sizeof(N10_LDT_ENTRY3DOLLAR_4E) == 4, sizeof(N10_LDT_ENTRY3DOLLAR_4E)
assert alignment(N10_LDT_ENTRY3DOLLAR_4E) == 4, alignment(N10_LDT_ENTRY3DOLLAR_4E)
_LDT_ENTRY._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1661
    ('LimitLow', WORD),
    ('BaseLow', WORD),
    ('HighWord', N10_LDT_ENTRY3DOLLAR_4E),
]
assert sizeof(_LDT_ENTRY) == 8, sizeof(_LDT_ENTRY)
assert alignment(_LDT_ENTRY) == 4, alignment(_LDT_ENTRY)
PVOID = c_void_p
UINT_PTR = c_ulong
SIZE_T = UINT_PTR
_MEMORY_BASIC_INFORMATION._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 4534
    ('BaseAddress', PVOID),
    ('AllocationBase', PVOID),
    ('AllocationProtect', DWORD),
    ('RegionSize', SIZE_T),
    ('State', DWORD),
    ('Protect', DWORD),
    ('Type', DWORD),
]
if is_64bits:
    assert sizeof(_MEMORY_BASIC_INFORMATION) == 40, sizeof(_MEMORY_BASIC_INFORMATION)
    assert alignment(_MEMORY_BASIC_INFORMATION) == 8, alignment(_MEMORY_BASIC_INFORMATION)
else:
    assert sizeof(_MEMORY_BASIC_INFORMATION) == 28, sizeof(_MEMORY_BASIC_INFORMATION)
    assert alignment(_MEMORY_BASIC_INFORMATION) == 4, alignment(_MEMORY_BASIC_INFORMATION)

# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1539
class _FLOATING_SAVE_AREA(Structure):
    pass
_FLOATING_SAVE_AREA._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1539
    ('ControlWord', DWORD),
    ('StatusWord', DWORD),
    ('TagWord', DWORD),
    ('ErrorOffset', DWORD),
    ('ErrorSelector', DWORD),
    ('DataOffset', DWORD),
    ('DataSelector', DWORD),
    ('RegisterArea', BYTE * 80),
    ('Cr0NpxState', DWORD),
]
assert sizeof(_FLOATING_SAVE_AREA) == 112, sizeof(_FLOATING_SAVE_AREA)
assert alignment(_FLOATING_SAVE_AREA) == 4, alignment(_FLOATING_SAVE_AREA)
FLOATING_SAVE_AREA = _FLOATING_SAVE_AREA
_CONTEXT._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 1563
    ('ContextFlags', DWORD),
    ('Dr0', DWORD),
    ('Dr1', DWORD),
    ('Dr2', DWORD),
    ('Dr3', DWORD),
    ('Dr6', DWORD),
    ('Dr7', DWORD),
    ('FloatSave', FLOATING_SAVE_AREA),
    ('SegGs', DWORD),
    ('SegFs', DWORD),
    ('SegEs', DWORD),
    ('SegDs', DWORD),
    ('Edi', DWORD),
    ('Esi', DWORD),
    ('Ebx', DWORD),
    ('Edx', DWORD),
    ('Ecx', DWORD),
    ('Eax', DWORD),
    ('Ebp', DWORD),
    ('Eip', DWORD),
    ('SegCs', DWORD),
    ('EFlags', DWORD),
    ('Esp', DWORD),
    ('SegSs', DWORD),
    ('ExtendedRegisters', BYTE * 512),
]
assert sizeof(_CONTEXT) == 716, sizeof(_CONTEXT)
assert alignment(_CONTEXT) == 4, alignment(_CONTEXT)

DWORD64 = c_ulonglong


# Define 128-bit 16-byte aligned xmm register type.
class M128A(Structure):
    _pack_ = 16
    _fields_ = [
        ("Low", DWORD64),
        ("High", DWORD64),
        ]

class DUMMYSTRUCTNAME(Structure):
    _fields_ = [
        ("Header", M128A * 2),
        ("Legacy", M128A * 8),
        ("Xmm0", M128A),
        ("Xmm1", M128A),
        ("Xmm2", M128A),
        ("Xmm3", M128A),
        ("Xmm4", M128A),
        ("Xmm5", M128A),
        ("Xmm6", M128A),
        ("Xmm7", M128A),
        ("Xmm8", M128A),
        ("Xmm9", M128A),
        ("Xmm10", M128A),
        ("Xmm11", M128A),
        ("Xmm12", M128A),
        ("Xmm13", M128A),
        ("Xmm14", M128A),
        ("Xmm15", M128A),
    ]

class _XSAVE_FORMAT32(Structure):
    # align 16
    _fields_ = [
        ("ControlWord", WORD),
        ("StatusWord",WORD),
        ("TagWord",BYTE),
        ("Reserved1",BYTE),
        ("ErrorOpcode",WORD),
        ("ErrorOffset",DWORD),
        ("ErrorSelector",WORD),
        ("Reserved2",WORD),
        ("DataOffset",DWORD),
        ("DataSelector",WORD),
        ("Reserved3",WORD),
        ("MxCsr",DWORD),
        ("MxCsr_Mask",DWORD),
        ("FloatRegisters",M128A*8),

        ("XmmRegisters",M128A*8),
        ("Reserved4",BYTE*192),
        ("StackControl", DWORD*7),   # KERNEL_STACK_CONTROL structure actualy
        ("Cr0NpxState",DWORD),
        ]

class _XSAVE_FORMAT64(Structure):
    # align 16
    _fields_ = [
        ("ControlWord", WORD),
        ("StatusWord",WORD),
        ("TagWord",BYTE),
        ("Reserved1",BYTE),
        ("ErrorOpcode",WORD),
        ("ErrorOffset",DWORD),
        ("ErrorSelector",WORD),
        ("Reserved2",WORD),
        ("DataOffset",DWORD),
        ("DataSelector",WORD),
        ("Reserved3",WORD),
        ("MxCsr",DWORD),
        ("MxCsr_Mask",DWORD),
        ("FloatRegisters",M128A*8),

        ("XmmRegisters",M128A*16),
        ("Reserved4",BYTE*96),
        ]

if is_64bits:
    XSAVE_FORMAT = _XSAVE_FORMAT64
else:
    XSAVE_FORMAT = _XSAVE_FORMAT32
XMM_SAVE_AREA32 = XSAVE_FORMAT

class DUMMYUNIONNAME(Union):
    _fields_ = [
        ("FltSave", XMM_SAVE_AREA32),
        ("DummyStructName", DUMMYSTRUCTNAME)
    ]

class _CONTEXT64(Structure):
    _pack_ = 16
    _fields_ = [
        ("P1Home", DWORD64),
        ("P2Home", DWORD64),
        ("P3Home", DWORD64),
        ("P4Home", DWORD64),
        ("P5Home", DWORD64),
        ("P6Home", DWORD64),

        ("ContextFlags", DWORD),
        ("MxCsr", DWORD),

        ("SegCs", WORD),
        ("SegDs", WORD),
        ("SegEs", WORD),
        ("SegFs", WORD),
        ("SegGs", WORD),
        ("SegSs", WORD),
        ("EFlags", DWORD),

        ("Dr0", DWORD64),
        ("Dr1", DWORD64),
        ("Dr2", DWORD64),
        ("Dr3", DWORD64),
        ("Dr6", DWORD64),
        ("Dr7", DWORD64),

        ("Rax", DWORD64),
        ("Rcx", DWORD64),
        ("Rdx", DWORD64),
        ("Rbx", DWORD64),
        ("Rsp", DWORD64),
        ("Rbp", DWORD64),
        ("Rsi", DWORD64),
        ("Rdi", DWORD64),
        ("R8", DWORD64),
        ("R9", DWORD64),
        ("R10", DWORD64),
        ("R11", DWORD64),
        ("R12", DWORD64),
        ("R13", DWORD64),
        ("R14", DWORD64),
        ("R15", DWORD64),
        ("Rip", DWORD64),

        ("DebugControl", DWORD64),
        ("LastBranchToRip", DWORD64),
        ("LastBranchFromRip", DWORD64),
        ("LastExceptionToRip", DWORD64),
        ("LastExceptionFromRip", DWORD64),

        ("DUMMYUNIONNAME", DUMMYUNIONNAME),

        ("VectorRegister", M128A * 26),
        ("VectorControl", DWORD64),

        ("DebugControl", DWORD),
        ("LastBranchToRip", DWORD),
        ("LastBranchFromRip", DWORD),
        ("LastExceptionToRip", DWORD),
        ("LastExceptionFromRip", DWORD)
]
####### TODO: BROKEN
###############assert alignment(_CONTEXT64) == 16, alignment(_CONTEXT64)
assert sizeof(_CONTEXT64) == 1256, sizeof(_CONTEXT64)
CONTEXT64 = _CONTEXT64

# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 498
class N12_SYSTEM_INFO4DOLLAR_37E(Union):
    pass
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 500
class N12_SYSTEM_INFO4DOLLAR_374DOLLAR_38E(Structure):
    pass
N12_SYSTEM_INFO4DOLLAR_374DOLLAR_38E._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 500
    ('wProcessorArchitecture', WORD),
    ('wReserved', WORD),
]
assert sizeof(N12_SYSTEM_INFO4DOLLAR_374DOLLAR_38E) == 4, sizeof(N12_SYSTEM_INFO4DOLLAR_374DOLLAR_38E)
assert alignment(N12_SYSTEM_INFO4DOLLAR_374DOLLAR_38E) == 2, alignment(N12_SYSTEM_INFO4DOLLAR_374DOLLAR_38E)
N12_SYSTEM_INFO4DOLLAR_37E._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 498
    ('dwOemId', DWORD),
    # Unnamed field renamed to '_'
    ('_', N12_SYSTEM_INFO4DOLLAR_374DOLLAR_38E),
]
assert sizeof(N12_SYSTEM_INFO4DOLLAR_37E) == 4, sizeof(N12_SYSTEM_INFO4DOLLAR_37E)
assert alignment(N12_SYSTEM_INFO4DOLLAR_37E) == 4, alignment(N12_SYSTEM_INFO4DOLLAR_37E)
LPVOID = c_void_p
_SYSTEM_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 497
    # Unnamed field renamed to '_'
    ('_', N12_SYSTEM_INFO4DOLLAR_37E),
    ('dwPageSize', DWORD),
    ('lpMinimumApplicationAddress', LPVOID),
    ('lpMaximumApplicationAddress', LPVOID),
    ('dwActiveProcessorMask', DWORD),
    ('dwNumberOfProcessors', DWORD),
    ('dwProcessorType', DWORD),
    ('dwAllocationGranularity', DWORD),
    ('wProcessorLevel', WORD),
    ('wProcessorRevision', WORD),
]
if is_64bits:
    assert sizeof(_SYSTEM_INFO) == 48, sizeof(_SYSTEM_INFO)
    assert alignment(_SYSTEM_INFO) == 8, alignment(_SYSTEM_INFO)
else:
    assert sizeof(_SYSTEM_INFO) == 36, sizeof(_SYSTEM_INFO)
    assert alignment(_SYSTEM_INFO) == 4, alignment(_SYSTEM_INFO)
CHAR = c_char
LPSTR = POINTER(CHAR)
LPBYTE = POINTER(BYTE)
_STARTUPINFOA._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 3774
    ('cb', DWORD),
    ('lpReserved', LPSTR),
    ('lpDesktop', LPSTR),
    ('lpTitle', LPSTR),
    ('dwX', DWORD),
    ('dwY', DWORD),
    ('dwXSize', DWORD),
    ('dwYSize', DWORD),
    ('dwXCountChars', DWORD),
    ('dwYCountChars', DWORD),
    ('dwFillAttribute', DWORD),
    ('dwFlags', DWORD),
    ('wShowWindow', WORD),
    ('cbReserved2', WORD),
    ('lpReserved2', LPBYTE),
    ('hStdInput', HANDLE),
    ('hStdOutput', HANDLE),
    ('hStdError', HANDLE),
]
if is_64bits:
    assert sizeof(_STARTUPINFOA) == 104, sizeof(_STARTUPINFOA)
    assert alignment(_STARTUPINFOA) == 8, alignment(_STARTUPINFOA)
else:
    assert sizeof(_STARTUPINFOA) == 68, sizeof(_STARTUPINFOA)
    assert alignment(_STARTUPINFOA) == 4, alignment(_STARTUPINFOA)

# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 701
class N12_DEBUG_EVENT4DOLLAR_39E(Union):
    pass
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 640
class _EXCEPTION_DEBUG_INFO(Structure):
    pass
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 3101
class _EXCEPTION_RECORD32(Structure):
    pass
_EXCEPTION_RECORD32._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 3101
    ('ExceptionCode', DWORD),
    ('ExceptionFlags', DWORD),
    ('ExceptionRecord', POINTER(_EXCEPTION_RECORD32)),
    ('ExceptionAddress', PVOID),
    ('NumberParameters', DWORD),
    ('ExceptionInformation', UINT_PTR * 15),
]
class _EXCEPTION_RECORD64(Structure):
    pass
_EXCEPTION_RECORD64._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 3101
    ('ExceptionCode', DWORD),
    ('ExceptionFlags', DWORD),
    ('ExceptionRecord', POINTER(_EXCEPTION_RECORD64)), # == DWORD64
    ('ExceptionAddress', PVOID), # == DWORD64
    ('NumberParameters', DWORD),
    ( 'UnusedAlignment', DWORD),
    ('ExceptionInformation', DWORD64 * 15),
]

# https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-exception_record
if is_64bits:
    EXCEPTION_RECORD = _EXCEPTION_RECORD64
    assert sizeof(_EXCEPTION_RECORD64) == 152, sizeof(_EXCEPTION_RECORD64)
    assert alignment(_EXCEPTION_RECORD64) == 8, alignment(_EXCEPTION_RECORD64)
else:
    EXCEPTION_RECORD = _EXCEPTION_RECORD32
    assert sizeof(_EXCEPTION_RECORD32) == 80, sizeof(_EXCEPTION_RECORD32)
    assert alignment(_EXCEPTION_RECORD32) == 4, alignment(_EXCEPTION_RECORD32)


_EXCEPTION_DEBUG_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 640
    ('ExceptionRecord', EXCEPTION_RECORD),
    ('dwFirstChance', DWORD),
]
if is_64bits:
    assert sizeof(_EXCEPTION_DEBUG_INFO) == 160, sizeof(_EXCEPTION_DEBUG_INFO)
    assert alignment(_EXCEPTION_DEBUG_INFO) == 8, alignment(_EXCEPTION_DEBUG_INFO)
else:
    assert sizeof(_EXCEPTION_DEBUG_INFO) == 84, sizeof(_EXCEPTION_DEBUG_INFO)
    assert alignment(_EXCEPTION_DEBUG_INFO) == 4, alignment(_EXCEPTION_DEBUG_INFO)
EXCEPTION_DEBUG_INFO = _EXCEPTION_DEBUG_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 645
class _CREATE_THREAD_DEBUG_INFO(Structure):
    pass

# macos compatability.
try:
    PTHREAD_START_ROUTINE = WINFUNCTYPE(DWORD, c_void_p)
except:
    PTHREAD_START_ROUTINE = CFUNCTYPE(DWORD, c_void_p)

LPTHREAD_START_ROUTINE = PTHREAD_START_ROUTINE
_CREATE_THREAD_DEBUG_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 645
    ('hThread', HANDLE),
    ('lpThreadLocalBase', LPVOID),
    ('lpStartAddress', LPTHREAD_START_ROUTINE),
]
if is_64bits:
    assert sizeof(_CREATE_THREAD_DEBUG_INFO) == 24, sizeof(_CREATE_THREAD_DEBUG_INFO)
    assert alignment(_CREATE_THREAD_DEBUG_INFO) == 8, alignment(_CREATE_THREAD_DEBUG_INFO)
else:
    assert sizeof(_CREATE_THREAD_DEBUG_INFO) == 12, sizeof(_CREATE_THREAD_DEBUG_INFO)
    assert alignment(_CREATE_THREAD_DEBUG_INFO) == 4, alignment(_CREATE_THREAD_DEBUG_INFO)
CREATE_THREAD_DEBUG_INFO = _CREATE_THREAD_DEBUG_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 651
class _CREATE_PROCESS_DEBUG_INFO(Structure):
    pass
_CREATE_PROCESS_DEBUG_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 651
    ('hFile', HANDLE),
    ('hProcess', HANDLE),
    ('hThread', HANDLE),
    ('lpBaseOfImage', LPVOID),
    ('dwDebugInfoFileOffset', DWORD),
    ('nDebugInfoSize', DWORD),
    ('lpThreadLocalBase', LPVOID),
    ('lpStartAddress', LPTHREAD_START_ROUTINE),
    ('lpImageName', LPVOID),
    ('fUnicode', WORD),
]
if is_64bits:
    assert sizeof(_CREATE_PROCESS_DEBUG_INFO) == 72, sizeof(_CREATE_PROCESS_DEBUG_INFO)
    assert alignment(_CREATE_PROCESS_DEBUG_INFO) == 8, alignment(_CREATE_PROCESS_DEBUG_INFO)
else:
    assert sizeof(_CREATE_PROCESS_DEBUG_INFO) == 40, sizeof(_CREATE_PROCESS_DEBUG_INFO)
    assert alignment(_CREATE_PROCESS_DEBUG_INFO) == 4, alignment(_CREATE_PROCESS_DEBUG_INFO)
CREATE_PROCESS_DEBUG_INFO = _CREATE_PROCESS_DEBUG_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 664
class _EXIT_THREAD_DEBUG_INFO(Structure):
    pass
_EXIT_THREAD_DEBUG_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 664
    ('dwExitCode', DWORD),
]
assert sizeof(_EXIT_THREAD_DEBUG_INFO) == 4, sizeof(_EXIT_THREAD_DEBUG_INFO)
assert alignment(_EXIT_THREAD_DEBUG_INFO) == 4, alignment(_EXIT_THREAD_DEBUG_INFO)
EXIT_THREAD_DEBUG_INFO = _EXIT_THREAD_DEBUG_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 668
class _EXIT_PROCESS_DEBUG_INFO(Structure):
    pass
_EXIT_PROCESS_DEBUG_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 668
    ('dwExitCode', DWORD),
]
assert sizeof(_EXIT_PROCESS_DEBUG_INFO) == 4, sizeof(_EXIT_PROCESS_DEBUG_INFO)
assert alignment(_EXIT_PROCESS_DEBUG_INFO) == 4, alignment(_EXIT_PROCESS_DEBUG_INFO)
EXIT_PROCESS_DEBUG_INFO = _EXIT_PROCESS_DEBUG_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 672
class _LOAD_DLL_DEBUG_INFO(Structure):
    pass
_LOAD_DLL_DEBUG_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 672
    ('hFile', HANDLE),
    ('lpBaseOfDll', LPVOID),
    ('dwDebugInfoFileOffset', DWORD),
    ('nDebugInfoSize', DWORD),
    ('lpImageName', LPVOID),
    ('fUnicode', WORD),
]
if is_64bits:
    assert sizeof(_LOAD_DLL_DEBUG_INFO) == 40, sizeof(_LOAD_DLL_DEBUG_INFO)
    assert alignment(_LOAD_DLL_DEBUG_INFO) == 8, alignment(_LOAD_DLL_DEBUG_INFO)
else:
    assert sizeof(_LOAD_DLL_DEBUG_INFO) == 24, sizeof(_LOAD_DLL_DEBUG_INFO)
    assert alignment(_LOAD_DLL_DEBUG_INFO) == 4, alignment(_LOAD_DLL_DEBUG_INFO)
LOAD_DLL_DEBUG_INFO = _LOAD_DLL_DEBUG_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 681
class _UNLOAD_DLL_DEBUG_INFO(Structure):
    pass
_UNLOAD_DLL_DEBUG_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 681
    ('lpBaseOfDll', LPVOID),
]
if is_64bits:
    assert sizeof(_UNLOAD_DLL_DEBUG_INFO) == 8, sizeof(_UNLOAD_DLL_DEBUG_INFO)
    assert alignment(_UNLOAD_DLL_DEBUG_INFO) == 8, alignment(_UNLOAD_DLL_DEBUG_INFO)
else:
    assert sizeof(_UNLOAD_DLL_DEBUG_INFO) == 4, sizeof(_UNLOAD_DLL_DEBUG_INFO)
    assert alignment(_UNLOAD_DLL_DEBUG_INFO) == 4, alignment(_UNLOAD_DLL_DEBUG_INFO)
UNLOAD_DLL_DEBUG_INFO = _UNLOAD_DLL_DEBUG_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 685
class _OUTPUT_DEBUG_STRING_INFO(Structure):
    pass
_OUTPUT_DEBUG_STRING_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 685
    ('lpDebugStringData', LPSTR),
    ('fUnicode', WORD),
    ('nDebugStringLength', WORD),
]
if is_64bits:
    assert sizeof(_OUTPUT_DEBUG_STRING_INFO) == 16, sizeof(_OUTPUT_DEBUG_STRING_INFO)
    assert alignment(_OUTPUT_DEBUG_STRING_INFO) == 8, alignment(_OUTPUT_DEBUG_STRING_INFO)
else:
    assert sizeof(_OUTPUT_DEBUG_STRING_INFO) == 8, sizeof(_OUTPUT_DEBUG_STRING_INFO)
    assert alignment(_OUTPUT_DEBUG_STRING_INFO) == 4, alignment(_OUTPUT_DEBUG_STRING_INFO)
OUTPUT_DEBUG_STRING_INFO = _OUTPUT_DEBUG_STRING_INFO
# C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 691
class _RIP_INFO(Structure):
    pass
_RIP_INFO._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 691
    ('dwError', DWORD),
    ('dwType', DWORD),
]
assert sizeof(_RIP_INFO) == 8, sizeof(_RIP_INFO)
assert alignment(_RIP_INFO) == 4, alignment(_RIP_INFO)
RIP_INFO = _RIP_INFO
N12_DEBUG_EVENT4DOLLAR_39E._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 701
    ('Exception', EXCEPTION_DEBUG_INFO),
    ('CreateThread', CREATE_THREAD_DEBUG_INFO),
    ('CreateProcessInfo', CREATE_PROCESS_DEBUG_INFO),
    ('ExitThread', EXIT_THREAD_DEBUG_INFO),
    ('ExitProcess', EXIT_PROCESS_DEBUG_INFO),
    ('LoadDll', LOAD_DLL_DEBUG_INFO),
    ('UnloadDll', UNLOAD_DLL_DEBUG_INFO),
    ('DebugString', OUTPUT_DEBUG_STRING_INFO),
    ('RipInfo', RIP_INFO),
]
if is_64bits:
    assert sizeof(N12_DEBUG_EVENT4DOLLAR_39E) == 160, sizeof(N12_DEBUG_EVENT4DOLLAR_39E)
    assert alignment(N12_DEBUG_EVENT4DOLLAR_39E) == 8, alignment(N12_DEBUG_EVENT4DOLLAR_39E)
else:
    assert sizeof(N12_DEBUG_EVENT4DOLLAR_39E) == 84, sizeof(N12_DEBUG_EVENT4DOLLAR_39E)
    assert alignment(N12_DEBUG_EVENT4DOLLAR_39E) == 4, alignment(N12_DEBUG_EVENT4DOLLAR_39E)
_DEBUG_EVENT._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 697
    ('dwDebugEventCode', DWORD),
    ('dwProcessId', DWORD),
    ('dwThreadId', DWORD),
    ('u', N12_DEBUG_EVENT4DOLLAR_39E),
]
if is_64bits:
    assert sizeof(_DEBUG_EVENT) == 176, sizeof(_DEBUG_EVENT)
    assert alignment(_DEBUG_EVENT) == 8, alignment(_DEBUG_EVENT)
else:
    assert sizeof(_DEBUG_EVENT) == 96, sizeof(_DEBUG_EVENT)
    assert alignment(_DEBUG_EVENT) == 4, alignment(_DEBUG_EVENT)
LONG = c_long
_LUID._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 394
    ('LowPart', DWORD),
    ('HighPart', LONG),
]
assert sizeof(_LUID) == 8, sizeof(_LUID)
assert alignment(_LUID) == 4, alignment(_LUID)
# C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 3241
class _LUID_AND_ATTRIBUTES(Structure):
    pass
_LUID_AND_ATTRIBUTES._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 3241
    ('Luid', LUID),
    ('Attributes', DWORD),
]
assert sizeof(_LUID_AND_ATTRIBUTES) == 12, sizeof(_LUID_AND_ATTRIBUTES)
assert alignment(_LUID_AND_ATTRIBUTES) == 4, alignment(_LUID_AND_ATTRIBUTES)
LUID_AND_ATTRIBUTES = _LUID_AND_ATTRIBUTES
_TOKEN_PRIVILEGES._fields_ = [
    # C:/PROGRA~1/gccxml/bin/Vc6/Include/winnt.h 4188
    ('PrivilegeCount', DWORD),
    ('Privileges', LUID_AND_ATTRIBUTES * 1),
]
assert sizeof(_TOKEN_PRIVILEGES) == 16, sizeof(_TOKEN_PRIVILEGES)
assert alignment(_TOKEN_PRIVILEGES) == 4, alignment(_TOKEN_PRIVILEGES)
_PROCESS_INFORMATION._fields_ = [
    # C:/PROGRA~1/MICROS~2/VC98/Include/winbase.h 229
    ('hProcess', HANDLE),
    ('hThread', HANDLE),
    ('dwProcessId', DWORD),
    ('dwThreadId', DWORD),
]
if is_64bits:
    assert sizeof(_PROCESS_INFORMATION) == 24, sizeof(_PROCESS_INFORMATION)
    assert alignment(_PROCESS_INFORMATION) == 8, alignment(_PROCESS_INFORMATION)
else:
    assert sizeof(_PROCESS_INFORMATION) == 16, sizeof(_PROCESS_INFORMATION)
    assert alignment(_PROCESS_INFORMATION) == 4, alignment(_PROCESS_INFORMATION)

class _IMAGE_FILE_HEADER(Structure):
    _fields_ = [
        ("Machine", WORD),
        ("NumberOfSections", WORD),
        ("TimeDateStamp", DWORD),
        ("PointerToSymbolTable", DWORD),
        ("NumberOfSymbols", DWORD),
        ("SizeOfOptionalHeader", WORD),
        ("Characteristics", WORD),
    ]

class _IMAGE_DATA_DIRECTORY(Structure):
    _fields_ = [
        ("VirtualAddress", DWORD),
        ("Size", DWORD),
    ]

class _IMAGE_DATA_DIRECTORY(Structure):
    _fields_ = [
        ("VirtualAddress", DWORD),
        ("Size", DWORD),
    ]

IMAGE_NUMBEROF_DIRECTORY_ENTRIES = 16

class _IMAGE_OPTIONAL_HEADER(Structure):
    _fields_ = [
        ("Magic", WORD),
        ("MajorLinkerVersion", BYTE),
        ("MinorLinkerVersion", BYTE),
        ("SizeOfCode", DWORD),
        ("SizeOfInitializedData", DWORD),
        ("SizeOfUninitializedData", DWORD),
        ("AddressOfEntryPoint", DWORD),
        ("BaseOfCode", DWORD),
        ("BaseOfData", DWORD),
        ("ImageBase", DWORD),
        ("SectionAlignment", DWORD),
        ("FileAlignment", DWORD),
        ("MajorOperatingSystemVersion", WORD),
        ("MinorOperatingSystemVersion", WORD),
        ("MajorImageVersion", WORD),
        ("MinorImageVersion", WORD),
        ("MajorSubsystemVersion", WORD),
        ("MinorSubsystemVersion", WORD),
        ("Win32VersionValue", DWORD),
        ("SizeOfImage", DWORD),
        ("SizeOfHeaders", DWORD),
        ("CheckSum", DWORD),
        ("Subsystem", WORD),
        ("DllCharacteristics", WORD),
        ("SizeOfStackReserve", DWORD),
        ("SizeOfStackCommit", DWORD),
        ("SizeOfHeapReserve", DWORD),
        ("SizeOfHeapCommit", DWORD),
        ("LoaderFlags", DWORD),
        ("NumberOfRvaAndSizes", DWORD),
        ("DataDirectory", _IMAGE_DATA_DIRECTORY * IMAGE_NUMBEROF_DIRECTORY_ENTRIES),
    ]
IMAGE_OPTIONAL_HEADER32 = _IMAGE_OPTIONAL_HEADER

class _IMAGE_OPTIONAL_HEADER64(Structure):
    _fields_ = [
        ("Magic", WORD),
        ("MajorLinkerVersion", BYTE),
        ("MinorLinkerVersion", BYTE),
        ("SizeOfCode", DWORD),
        ("SizeOfInitializedData", DWORD),
        ("SizeOfUninitializedData", DWORD),
        ("AddressOfEntryPoint", DWORD),
        ("BaseOfCode", DWORD),
        ("ImageBase", DWORD64),
        ("SectionAlignment", DWORD),
        ("FileAlignment", DWORD),
        ("MajorOperatingSystemVersion", WORD),
        ("MinorOperatingSystemVersion", WORD),
        ("MajorImageVersion", WORD),
        ("MinorImageVersion", WORD),
        ("MajorSubsystemVersion", WORD),
        ("MinorSubsystemVersion", WORD),
        ("Win32VersionValue", DWORD),
        ("SizeOfImage", DWORD),
        ("SizeOfHeaders", DWORD),
        ("CheckSum", DWORD),
        ("Subsystem", WORD),
        ("DllCharacteristics", WORD),
        ("SizeOfStackReserve", DWORD64),
        ("SizeOfStackCommit", DWORD64),
        ("SizeOfHeapReserve", DWORD64),
        ("SizeOfHeapCommit", DWORD64),
        ("LoaderFlags", DWORD),
        ("NumberOfRvaAndSizes", DWORD),
        ("DataDirectory", _IMAGE_DATA_DIRECTORY * IMAGE_NUMBEROF_DIRECTORY_ENTRIES),
    ]
IMAGE_OPTIONAL_HEADER64 = _IMAGE_OPTIONAL_HEADER64

