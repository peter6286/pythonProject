import random


def getenv(num):
    myDict = {}
    for i in range(0,num):
        myDict[i] = [i+1]
    myDict[num-1] = [0]
    #print(myDict[0])
    print(myDict)
    count = 0
    while count < 3:
        degree_in = random.randint(0, num-1)
        degree_out = random.randint(0, num-1)
        if len(myDict[degree_in])>3 or (degree_out in myDict[degree_in]) or (degree_in == degree_out) or (degree_in + 1 == degree_out):
            continue
        print(degree_in, degree_out)
        myDict[degree_in].append(degree_out)
        count += 1
    return myDict


print(getenv(10))