def my_function():
    print("Hello from a function")
#I created the function named my_function

def my_function():
    print("Hello from a function")
#Hello from a function

def my_function(fname, lname):
    print(fname)
#the code will print the first parameter

def my_function(x):
    return x+5
#5 will be added to the parameter x

def my_function(*kids):
  print("The youngest child is " + kids[2])
#* is a prefix, add when you don't know the number of arguments will be passed into your function

def my_function(**kid):
  print("His last name is " + kid["lname"])
#number of keyword arguments is unknown

