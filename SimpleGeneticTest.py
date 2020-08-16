from random import randrange

input = 1
output = 5

def formula(input,x):
  return input * x

def cross(a1, a2):
  #generate a cross of 1-5
  cross = randrange(5)+1
  binarya1 = a1[0:cross]
  binarya2 = a2[cross:6]
  return binarya1 + binarya2

def mutate(x):
  if randrange(2):
    bitToFlip = randrange(5)+1
    if x[bitToFlip] == '1':
      x = x[:bitToFlip] + '0' + x[bitToFlip+1:]
    else:
      x = x[:bitToFlip] + '1' + x[bitToFlip+1:]
    return x
  else:
    return x

def calculateError(x):
  return abs(output - formula(input, x))
  
a1 = "011101"
a2 = "101010"

best = a1
bestError = calculateError(int(a1, 2))
for i in range(1000):
  tempa1 = cross(a1,a2)
  tempa2 = cross(a1,a2)
  tempa1 = mutate(tempa1)
  tempa2 = mutate(tempa2)
  a1 = tempa1
  a2 = tempa2
  if calculateError(int(a1, 2)) < bestError:
    best = a1
    bestError = calculateError(int(a1, 2))
  if calculateError(int(a2, 2)) < bestError:
    best = a2
    bestError = calculateError(int(a2, 2))
print("Final Error = {}".format(bestError))
print("Final modifier = {}".format(int(best,2)))
print("Final modifier (in binary) = {}".format(best))
