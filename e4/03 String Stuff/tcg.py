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

rnd = lambda minimum=0, maximum=10**8: random.randint(minimum, maximum-1)

# Test-case generator template
# Example problem: Take n and m in first line
# and take n elements in second line
# print sum of n elements mod m

count = 0

def giveRandomInput():
    n, m = rnd(), rnd()
    s = ['+', '-', '*', '/'][rnd(0, 4)]
    return (str(n) + s + str(m))

def solveOut(inputs):
    (s) = inputs
    
    i = 0
    while('0' <= s[i] <= '9'): i+=1

    n = int(s[:i])
    m = int(s[i+1:])

    ans = 0
    if s[i] == '+':
        ans = n + m
    
    if s[i] == '-':
        ans = n - m
    
    if s[i] == '*':
        ans = n * m
    
    if s[i] == '/':
        ans = n // m


    return "{}".format(ans)

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
    s = '131+40'
    inputs = (s)
    
    inString = "{}\n".format(
        s
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    s = '27/2'
    inputs = (s)
    
    inString = "{}\n".format(
        s
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    print(i)
    inputs = giveRandomInput()
    (s) = inputs

    inString = "{}\n".format(
        s
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")