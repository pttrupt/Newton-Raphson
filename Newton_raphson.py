
# -*- coding: utf-8 -*-

#---------------------------------------------#
# Implementation of Newton-Raphson method 
#---------------------------------------------#

#Newton-Raphson for square root
# Find x such that x**2 -24 is within epsilon of 0

epsilon = 0.01
k = 24.0
guess = k / 2
iteration = 0

while abs(guess**2 - k) >= epsilon:
     iteration += 1
     guess = (1/2)* (guess + k/ guess)

print('Number of Guesses is', iteration)
print('Square root of', k, 'is about', guess)
