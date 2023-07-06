# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
import platform, struct

print(struct.calcsize("P") * 8)
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)