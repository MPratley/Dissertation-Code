# import numpy as np
# from Perceptron import Perceptron

# # PARAMS
# inputs = 10
# steps = 100
# inputFireOdds = 10 # input fire probability is 1/inputFireOdds
# randInputs = []

# # make the array of bit arrays representing the inputs
# for i in range(0, steps):
#     randArr = np.random.randint(inputFireOdds, size=inputs)
#     randInputs.append([int(not a) for a in randArr])

# p = Perceptron(inputs)

# print(p.output([0,0,0,0,0,0,0,0,0,0]))

from typing import Callable
import random

def testFunc(randGen:Callable[[],int]):
    print("num is: {}".format(randGen()))
    print("num is: {}".format(randGen()))

testFunc(lambda : random.randint(1,4))
testFunc(lambda: 3)