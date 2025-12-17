import math
num = 16
print("Square root: ",math.sqrt(num))
print("Factorial: ",math.factorial(5))

import os
print("Current Directory: ",os.getcwd())
print("Files in directory: ",os.listdir())
if not os.path.exists("demo"):
    os.mkdir("demo")
    print("Folder created")