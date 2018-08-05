#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep    
import mmap
import posix_ipc as ipc

s = ipc.SharedMemory('/shm', flags=ipc.O_CREAT, size=20, read_only=False)
mm = mmap.mmap(s.fd, s.size)
mm.seek(0)
mm.write(b'takara')
mm.write(b' aho maho')
mm.write(b' !\n')
s.close_fd()
sleep(600)

