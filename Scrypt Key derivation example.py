import binascii
import os
from passlib.hash import scrypt

passwd = "p@$$w0rD~3"
salt = os.urandom(32)
print("Salt: ", binascii.hexlify(salt))

key = scrypt.hash(passwd, salt, 16384, 8, 1, 32)
print("Derived key: ", binascii.hexlify(key))
 