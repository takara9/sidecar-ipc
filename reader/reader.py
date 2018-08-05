#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mmap
from time import sleep    
import posix_ipc as ipc

s = ipc.SharedMemory('/shm', flags=ipc.O_CREAT, size=20, read_only=False)
mm = mmap.mmap(s.fd, s.size)
mm.seek(0)
print mm.read(20)
sleep(600)
