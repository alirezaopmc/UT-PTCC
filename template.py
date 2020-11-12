import random

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
    n, x = random.randint(3, 10), random.randint(3, 11)
    a = [ random.randint(1, 101) for _ in range(n) ]
    return (n, a, x)

def solveOut(inputs):
    (n, a, x) = inputs
    
    ans = 0
    for i in range(n):
        ans = (ans + a[i]) % x

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
    n = 3
    a = [1, 11, 12]
    x = 5
    inputs = (n, a, x)
    
    inString = "{} {}\n{}\n".format(
        n, x,
        arrayToString(a)
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    inputs = giveRandomInput()
    (n, a, x) = inputs

    inString = "{} {}\n{}\n".format(
        n, x,
        arrayToString(a)
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")