import binascii
import secrets

import pbkdf2
import pyaes

plaintext = "Sample text for Encryption"
password = "s0m3p@$$w0rd"
key = pbkdf2.PBKDF2(password, 'some salt').read(16)
print('AES encryption key: ', binascii.hexlify(key))

iv = secrets.randbelow(2 << 128)
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('encrypted: ', binascii.hexlify(ciphertext))

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print('decrypted: ', decrypted)