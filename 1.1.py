import time

x = False

def true(true):
    print("X is true.")

def false(false):
    print("X is false.")


if x == True:
    true("true")

if x == False:
        false("false")

if x != False and x != True:
     print("x is " + x)

if x == True:
     while true:
          print("this statement is true because x is true")
          break

while x == False:
     print("x is false")
     time.sleep(5)
     print("x is \n" + x)
     break

# 9/17/26