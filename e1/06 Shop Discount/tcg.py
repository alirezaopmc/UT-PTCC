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
    m, a, b, c = random.randint(10, 1000), random.randint(5, 20), random.randint(1, 10), random.randint(5, 20)
    return (m, a, b, c)

def solveOut(inputs):
    (m, a, b, c) = inputs
    
    ans = m // c
    ans += (ans // a) * b

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
    (m, a, b, c) = (10, 3, 1, 1)
    inputs = (m, a, b, c)
    
    inString = "{} {} {} {}\n".format(
        m, a, b, c
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    inputs = giveRandomInput()
    (m, a, b, c) = inputs
    
    inString = "{} {} {} {}\n".format(
        m, a, b, c
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")