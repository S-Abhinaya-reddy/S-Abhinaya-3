# -*- coding: utf-8 -*-
"""Hash3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EE78m43yoRbak7jsTOnPzmeQoF_AB9FJ
"""

import hashlib

password = input("Enter any password:")
salt = input("Enter any extra password:")
new_password = (password+salt).encode()
count = int(input("Enter any number:"))
for i in range (count):
  new_password1 = bytes(str(new_password), 'utf-8')
  new = hashlib.md5(new_password1)
  print(new)

