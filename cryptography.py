"""
cryptography.py
Author: Matthew
Credit: Robbie

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"


Coding = True
while Coding:
    start = input("Enter e to encrypt, d to decrypt, or q to quit:")
    if start == "q":
        print("Goodbye")
        Coding = False
    else:
        print(start)

    