import ctypes

PROCESS_QUERY_INFORMATION = 0x400
PROCESS_VM_READ = 0x0010


# define the SYSTEM_INFO structure
class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [("wProcessorArchitecture", ctypes.c_uint16),
                ("wReserved", ctypes.c_uint16),
                ("dwPageSize", ctypes.c_uint32),
                ("lpMinimumApplicationAddress", ctypes.c_void_p),
                ("lpMaximumApplicationAddress", ctypes.c_void_p),
                ("dwActiveProcessorMask", ctypes.c_uint64),
                ("dwNumberOfProcessors", ctypes.c_uint32),
                ("dwProcessorType", ctypes.c_uint32),
                ("dwAllocationGranularity", ctypes.c_uint32),
                ("wProcessorLevel", ctypes.c_uint16),
                ("wProcessorRevision", ctypes.c_uint16)]

# define the PROCESS_BASIC_INFORMATION structure
class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [("Reserved1", ctypes.c_void_p),
                ("PebBaseAddress", ctypes.c_void_p),
                ("Reserved2", ctypes.c_void_p * 2),
                ("UniqueProcessId", ctypes.c_void_p),
                ("Reserved3", ctypes.c_void_p)]

# define the NTSTATUS type
NTSTATUS = ctypes.c_ulong

# define the ZwQueryInformationProcess function
def ZwQueryInformationProcess(ProcessHandle, ProcessInformationClass, ProcessInformation, ProcessInformationLength, ReturnLength=None):
    ntdll = ctypes.WinDLL("ntdll")
    return ntdll.ZwQueryInformationProcess(ProcessHandle, ProcessInformationClass, ProcessInformation, ProcessInformationLength, ReturnLength)

# define the GetSystemInfo function
def get_system_info():
    kernel32 = ctypes.WinDLL("kernel32")
    system_info = SYSTEM_INFO()
    kernel32.GetSystemInfo(ctypes.byref(system_info))
    return system_info

# define the get_process_teb function
def get_process_teb(process_handle):
    # get process PEB address
    process_basic_info = PROCESS_BASIC_INFORMATION()
    status = ZwQueryInformationProcess(process_handle, 0, ctypes.byref(process_basic_info), ctypes.sizeof(process_basic_info))
    if status != 0:
        raise ctypes.WinError(status)

    # calculate process TEB address
    system_info = get_system_info()
    teb_size = 0x1000 if system_info.wProcessorArchitecture == 9 else 0x2000
    teb_address = process_basic_info.PebBaseAddress + teb_size

    return teb_address, process_basic_info.PebBaseAddress# + 0x4000