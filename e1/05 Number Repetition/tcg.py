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
    n = random.randint(1, 1000)
    k = random.randint(1, n)
    return (n, k)

def solveOut(inputs):
    (n, k) = inputs
    
    ans = k * (n - k + 1)

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
    n, k = 1, 1
    inputs = (n, k)
    
    inString = "{} {}\n".format(
        n, k
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n, k = 4, 3
    inputs = (n, k)
    
    inString = "{} {}\n".format(
        n, k
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    inputs = giveRandomInput()
    (n, k) = inputs

    inString = "{} {}\n".format(
        n, k
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")