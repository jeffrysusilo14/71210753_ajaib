import time
from tkinter import N, Y

def ajaibrek(x):
    if x<=5:
        return x
    else:
        return ajaibrek(x-2)+ajaibrek(x//2)    

print(ajaibrek(10))

def ajaibit(x):
    for i in range (6,101,1):
        