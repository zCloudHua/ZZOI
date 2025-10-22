from random import randint

with open("Config.ini","a+") as file:
    file.write("10\n")
    for i in range(1,11):
        file.write(f"input{i}.txt|output{i}.txt|1|10|65536\n")