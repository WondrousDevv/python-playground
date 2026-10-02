import time
import random


def randomx():
     choice_type = random.choice(["int", "bool"])

     if choice_type == int:
          return random.randint(1, 10)
     else:
          return random.choice([True, False])
          
x = randomx()

def tru(tru):
    print("X is true.")

def fals(fals):
    print("X is false.")

if x == True:
    tru("true")

if x == False:
        fals("false")

if x != False and x != True:
     print("x is not a boolean")
     time.sleep(.5)
     print("therefore, x is " + str(x))

# 9/22/26