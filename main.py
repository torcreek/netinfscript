#!/usr/bin/env python3

from backaupnet_tool import Backup
from modules.devices import Device

import os
import psutil


# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


# decorator function
def profile(func):
    def wrapper(*args, **kwargs):

        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))

        return result
    return wrapper


@profile
def main():
    
    data = Backup()
    data.create_devices()
    print(Device.devices_lst)

if __name__ == "__main__":
    main()