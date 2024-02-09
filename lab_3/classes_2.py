#1
class stringM:
    def __init__(self):
        self.input_string = "" 
    def getStr(self):
        self.input_string = input("Enter a string: ")
    def printStr(self):
        print(self.input_string.upper())
# usage: 
string_manipulator = StringM()
string_manipulator.getStr()
string_manipulator.printStr()


#2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

# Usage:
shape_obj = Shape()
square_obj = Square(5)

print(shape_obj.area())    # Output: 0
print(square_obj.area())  # Output: 25


#3
class Rectangle(Shape):  
    def __init__(self, length, width):
        super().__init__()  
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
# Usage:
rectangle_obj = Rectangle(4, 6)
print("Area of Rectangle:", rectangle_obj.area())  # Output: 24


#4
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f({self.x}, {self.y})) #a method show to display the coordinates of the point

    def move(self, new_x, new_y): # method move to change these coordinates
        self.x = new_x
        self.y = new_y
    def dist(self, other_point): #a method dist that computes the distance between 2 points


        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
# Ussage:
point1 = point(1, 2)
point2 = point(4, 6)
point1.show()                 
point2.show()                

point1.move(3, 5)
point1.show()                 
distance = point1.dist(point2)
print(f{distance})  

#5
class account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal not allowed.")

#Usage:
account = Account(owner="John Doe", balance=1000)

account.deposit(500)    # Output: Deposit of 500 successful. New balance: 1500
account.withdraw(200)   # Output: Withdrawal of 200 successful. New balance: 1300
account.withdraw(1500)  # Output: Insufficient funds. Withdrawal not allowed.

#6
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: prime(x), numbers))
print(prime_numbers)