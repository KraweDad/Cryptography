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
    start = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if start != "q":
        if start == "e":
            a = []
            b = []
            f = []
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
                if q > 84:
                    o = q-84
                    f.append(o)
                else:
                    f.append(q)
            
            for h in f:
                wow = associations[h] #Converting letters back into #'s
                print(wow, end="") #Printing result
            print()
        elif start == "d":
            u = []
            z = []
            w = []
            m = input("Message: ")
            for c in m:
                n  = (associations.find(c))
                w.append(n) #converting message to #'s
            k = input("Key: ")
            for c in k:
                j = (associations.find(c))
                z.append(j) #converting key to #'s
            p = z*20    
            for l in range(len(m)):
                q = w[l] - p[l] #adding key's #'s to message #'s
                if q < 0:
                    o = q + 84
                    u.append(o)
                else:
                    u.append(q)
            
            for h in u:
                wow = associations[h] #Converting letters back into #'s
                print(wow, end="") #Printing result
            print()
        else:
            print("Did not understand command, try again.")
    else:
        print("Goodbye!")
        Coding = False
    
    
    

    
