"""
cryptography.py
Author: Matthew
Credit: Robbie

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"


a = []
b = []
f = []
Coding = True
while Coding:
    start = input("Enter e to encrypt, d to decrypt, or q to quit:")
    if start != "q":
        if start == "e":
            m = input("Message: ")
            for c in m:
                n  = (associations.find(c))
                a.append(n) #converting message to #'s
            k = input("Key: ")
            for c in k:
                j = (associations.find(c))
                b.append(j) #converting key to #'s
            p = b*20    
            for l in range(len(m)):
                q = a[l] + p[l] #adding key's #'s to message #'s
                f.append(q)
            for h in f:
                wow = associations[h] #Converting letters back into #'s
                print(wow, end="") #Printing result
            print()
        elif start == "d":
            print("Matt! focus on encrypting!")
        else:
            print("Matt its e not " + start + " you idiot")
    else:
        print("YOU'RE NOT ALLOWED TO QUIT YET")
        Coding = False
    
    
    

    
