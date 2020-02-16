import numpy as np 
import random, os

learning_rate = 1
bias = 1
# weights for the two inputs and one for the bias
weights = [random.random(), random.random(), random.random()]

def Perceptron(input1, input2, desired_output) :
    actual_output = input1 * weights[0] + input2 * weights[1] + bias*weights[2]

    # step function
    if actual_output > 0 :
        actual_output = 1
    else :
        actual_output = 0
    
    # adjusting weights based on error value
    error = desired_output - actual_output
    weights[0] += error * input1 * learning_rate
    weights[1] += error * input2 * learning_rate
    weights[2] += error * bias * learning_rate

    return actual_output

# learning with OR gate inputs
for i in range(50) :
    Perceptron(0,0,0)
    Perceptron(0,1,1)
    Perceptron(1,0,1)
    Perceptron(1,1,1)

# testing with user input
while True :
    x = int(input("Input value of x: "))
    y = int(input("Input value of y: "))
    expected = int(input("What should the OR gate result be? Input 1 for true or 0 for false: "))

    print(Perceptron(x,y,expected))
    
    if input("Would you like to exit? y/n: ") == 'y' :
        break
        