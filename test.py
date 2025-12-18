from numpy import *

x	= uint8(0b00101_000) # 5
y = uint8(0b00011_000) # 3
z = (uint16(x) << 3) // y
print(z / (1 << 3))
