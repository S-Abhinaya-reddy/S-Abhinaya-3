import hashlib
str_1 = input("Enter any object:")
print(hashlib.md5(str_1.encode()))
print(hashlib.sha1(str_1.encode()))
print(hashlib.sha512(str_1.encode()))
print(hashlib.sha256(str_1.encode()))

