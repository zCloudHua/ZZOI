from random import randint, sample

pokers = ["DA","CA","HA","SA","D2","C2","H2","S2","D3","C3","H3","S3","D4","C4","H4","S4","D5","C5","H5","S5","D6","C6","H6","S6","D7","C7","H7","S7","D8","C8","H8","S8","D9","C9","H9","S9","DT","CT","HT","ST","DJ","CJ","HJ","SJ","DQ","CQ","HQ","SQ","DK","CK","HK","SK"]

use_pokers = []

numbers = list(range(0, 52))

#print(len(numbers))

use_numbers = []

def make_2to4():
    for i in range(2,5):
        n = randint(20,52)
        use_pokers = sample(pokers, n)
        with open("Input/"+"input"+str(i)+".txt","a+") as file:
            file.write(str(n)+"\n")
            for j in use_pokers:
                file.write(j+"\n")

def make_5to7():
    for i in range(5,8):
        n = randint(20,52)
        use_numbers = sample(numbers, n)
        use_numbers.sort()
        with open("Input/"+"input"+str(i)+".txt","a+") as file:
            file.write(str(n)+"\n")
            for j in use_numbers:
                file.write(pokers[j]+"\n")

def make_8to10():
    for i in range(8,11):
        n = randint(20,52)
        with open("Input/"+"input"+str(i)+".txt","a+") as file:
            file.write(str(n)+"\n")
            for j in range(n):
                num = randint(0,51)
                file.write(pokers[num]+"\n")

#make_2to4()
#make_5to7()
#make_8to10()
