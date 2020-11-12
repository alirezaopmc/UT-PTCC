import random
import numpy as np

print(1)

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
    A = [ [ random.randint(-1000, 1001) for __ in range(3) ] for _ in range(3) ]
    D = [ random.randint(-1000, 1001) for __ in range(3) ]
    return (A, D)

def solveOut(inputs):
    (A, D) = inputs
    
    Matrix = np.array(A)
    Consts = np.array(D)
    Answer = np.linalg.solve(Matrix, Consts)

    return "{:.3f} {:.3f} {:.3f}\n".format(Answer[0],Answer[1],Answer[2])

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
    (A, D) = (
        [
            [1, 1, 1],
            [1, -1, 1],
            [2, -1, 0]
        ],
        [4, 2, 2]
    )
    inputs = (A, D)
    
    inString = "{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n".format(
        A[0][0], A[0][1], A[0][2], D[0],
        A[1][0], A[1][1], A[1][2], D[1],
        A[2][0], A[2][1], A[2][2], D[2]
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    inputs = giveRandomInput()
    (A, D) = inputs

    inputs = (A, D)
    
    inString = "{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n".format(
        A[0][0], A[0][1], A[0][2], D[0],
        A[1][0], A[1][1], A[1][2], D[1],
        A[2][0], A[2][1], A[2][2], D[2]
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")