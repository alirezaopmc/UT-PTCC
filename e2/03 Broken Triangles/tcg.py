import random
import math

# Utility functions
def arrayToString(arr: list):
    result: str = ""

    for i in range(len(arr)):
        if i + 1 < len(arr):
            result += "{} ".format(arr[i])
        else:
            result += "{}".format(arr[i])
    
    return result


# Test-case generator template
# Example problem: Take n and m in first line
# and take n elements in second line
# print sum of n elements mod m

count = 0

def giveRandomInput():
    n, m = random.randint(1, 101), random.randint(1, 101)
    c = ['a', '*', '!'][random.randint(0, 2)]
    return (n, m, c)

def solveOut(inputs):
    (n, m, c) = inputs
    
    res = ''
    for i in range(n):
        res += ' ' * (n - i - 1)
        for j in range(2*i+1):
            res += c if j != m-1 else ' '
        res += '\n'

    return res

def makeInputs(inString, cnt):
    path = "./in/input" + str(cnt) + ".txt"
    f = open(path, "w")
    f.write(inString)
    f.close()

def makeOutputs(outString, cnt):
    path = "./out/output" + str(cnt) + ".txt"
    f = open(path, "w")
    f.write(outString)
    f.close()

# Manually add some inputs
if "Case 1":
    n, m, c = 3, 1, '%'
    inputs = (n, m, c)
    
    inString = "{} {} {}\n".format(
        n, m, c
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n, m, c = 3, 2, 'Z'
    inputs = (n, m, c)
    
    inString = "{} {} {}\n".format(
        n, m, c
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    print(i)
    inputs = giveRandomInput()
    (n, m, c) = inputs

    inString = "{} {} {}\n".format(
        n, m, c
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")