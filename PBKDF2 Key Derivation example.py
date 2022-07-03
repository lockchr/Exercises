import binascii
import os
from backports.pbkdf2 import pbkdf2_hmac

salt = os.urandom(32)
passwd = "p@$$w0rD~3".encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 500000, 32)
print("Derived key:", binascii.hexlify(key))
