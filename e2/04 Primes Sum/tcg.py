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
    
# Is Prime?
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    
    return True


# Test-case generator template
# Example problem: Take n and m in first line
# and take n elements in second line
# print sum of n elements mod m

count = 0

def giveRandomInput():
    n = random.randint(1, 10000)
    return (n)

def solveOut(inputs):
    (n) = inputs
    
    ans = 0
    for i in range(2, n):
        if isPrime(i):
            ans += i

    return str(ans)

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
    n = 14
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 18
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    print(i)
    inputs = giveRandomInput()
    (n) = inputs

    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")