#data_maker for sqrt
#author:ZZA

from random import randint
import os
from math import sqrt

file_in = "Input"
file_out = "Output"
file_name = "sqrt"

def make_init():
    if not os.path.exists(file_in):
        os.makedirs(file_in)
    os.makedirs(file_out,exist_ok=True)
    with open("Config.ini", "w") as file:
        file.write("10\n")

def solve(input_file,output_file):
    with open(f"Input/{input_file}", "r") as file:
        lines = file.readlines()
    T = int(lines[0])
    with open(f"Output/{output_file}", "w") as file:
        for i in range(1, T+1):
            #print(T, len(lines))
            a = int(lines[i])
            b = int(sqrt(a))
            ans = (b-1)*3
            ans += int(a/b)-b+1
            file.write(f"{ans}\n")

def make1to2():
    for i in range(1, 3):
        with open(f"Input/{file_name}in{i}.in", "w") as file:
            n = 10
            file.write(f"{n}\n")
            for j in range(10):
                #a = randint(100000, 1000000)
                b = randint(315, 1000)
                a = b**2
                file.write(f"{a}\n")
        solve(f"{file_name}in{i}.in", f"{file_name}out{i}.ans")
        with open("Config.ini", "a") as file:
            file.write(f"{file_name}in{i}.in|{file_name}out{i}.ans|1|10|{512*1024}\n")

def make_then(st, ed, n, minn, maxn, flag):
    for i in range(st, ed+1):
        with open(f"Input/{file_name}in{i}.in", "w") as file:
            file.write(f"{n}\n")
            for j in range(n):
                if flag == True:
                    b = randint(int(sqrt(minn)), int(sqrt(maxn)))
                    a = b**2
                else:
                    a = randint(minn, maxn)
                file.write(f"{a}\n")
        solve(f"{file_name}in{i}.in", f"{file_name}out{i}.ans")
        with open("Config.ini", "a") as file:
            file.write(f"{file_name}in{i}.in|{file_name}out{i}.ans|1|10|{512*1024}\n")

"""
make_init()
make1to2()
"""

"""         
make_then(3, 3, 10, int(10**5), int(10**6), False)
make_then(4, 4, int(10**5), int(10**5), int(10**6), False)
"""

"""
make_then(5, 5, 10, int(10**10), int(10**11), True)
make_then(6, 6, int(10**5), int(10**10), int(10**11), True)
make_then(7, 8, int(10**5), int(10**10), int(10**11), False)
make_then(9, 10, int(10**5), int(10**16), int(10**18), False)
"""
