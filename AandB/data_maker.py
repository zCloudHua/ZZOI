from random import randint

inf = 10**9

for i in range(1,26):
    A = randint(-inf,inf)
    B = randint(-inf,inf)
    with open(f"AandB/AandB{i}.in","a+") as file:
        file.write(f"{A} {B}")
    with open(f"AandB/AandB{i}.out","a+") as file:
        file.write(f"{A+B}")
