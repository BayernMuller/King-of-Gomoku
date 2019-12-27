from ctypes import *
from console_pipe import *

pipe = console_pipe('Yixin.exe')

pipe.Write(b'START 15\r\nBEGIN\r\n')

while True:
	print(str(pipe.Read(1024)[1]))