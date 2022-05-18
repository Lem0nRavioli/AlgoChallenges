def ChessboardTraveling(str): 
    x, y, a, b = (int(str[1]), int(str[3]), int(str[6]), int(str[8]))
    rightSteps = a - x
    upSteps = b - y
    totalSteps = rightSteps + upSteps
    totalSteps_permutation = permutation(totalSteps)
    upSteps_permutation = permutation(upSteps)
    rightSteps_permutation = permutation(rightSteps)
    posibleSteps = int(totalSteps_permutation / (upSteps_permutation * rightSteps_permutation))
    return posibleSteps

def permutation(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
    
# keep this function call here  
print(ChessboardTraveling('(1 1)(3 3)'))
print(ChessboardTraveling('(1 1)(4 3)'))
print(ChessboardTraveling('(1 1)(3 4)'))
print(ChessboardTraveling('(1 1)(5 3)'))
print(ChessboardTraveling('(1 1)(3 7)'))
print(ChessboardTraveling('(1 1)(4 4)'))
print(ChessboardTraveling('(1 1)(5 5)'))
print(ChessboardTraveling('(1 1)(6 6)'))
print(ChessboardTraveling('(1 1)(7 7)'))
print(ChessboardTraveling('(1 1)(8 8)'))
