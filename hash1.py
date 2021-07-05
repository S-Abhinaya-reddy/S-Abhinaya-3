import hashlib
str_1 = input("Enter any onject:")
md5_value = hashlib.md5(str_1.encode())
print(md5_value)

