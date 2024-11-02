import mmap
import ctypes
from typing import Callable

class MemoryManager:
    def __init__(self):
        self.allocated_regions = []

    def allocate_executable_memory(self, size: int) -> mmap.mmap:
        """Allocate executable memory region."""
        memory = mmap.mmap(
            -1, size,
            flags=mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS,
            prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC
        )
        self.allocated_regions.append(memory)
        return memory

    def create_function_pointer(self, memory: mmap.mmap, restype=ctypes.c_double) -> Callable:
        """Create a callable function pointer from memory region."""
        func_type = ctypes.CFUNCTYPE(restype)
        return func_type(ctypes.cast(
            ctypes.c_void_p(ctypes.c_long.from_buffer(memory).value),
            func_type
        ))

    def cleanup(self):
        """Clean up all allocated memory regions."""
        for region in self.allocated_regions:
            try:
                region.close()
            except Exception as e:
                print(f"Warning: Failed to clean up memory region: {e}")
        self.allocated_regions.clear()

    def __del__(self):
        """Ensure cleanup on object destruction."""
        self.cleanup()