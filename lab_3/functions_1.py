#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#Usage:
grams_required = float(input())
ounces_result = grams_to_ounces(grams_required)
print(f{grams_required}, {ounces_result:.2f})



#2
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
#Usage
grams_required = 200
ounces_result = grams_to_ounces(grams_required)
print(f"{grams_required} grams is equal to {ounces_result:.2f} ounces")



#3
def solve(numheads, numlegs):
    if numlegs % 2 != 0 or numheads == 0 or numheads * 2 > numlegs or numheads * 4 < numlegs:
        return "No solution found"
    num_rabbits = (numlegs - (numheads * 2)) // 2
    num_chickens = numheads - num_rabbits
    return num_chickens, num_rabbits

#Usage:
num_heads = 35
num_legs = 94

result = solve(num_heads, num_legs)

if isinstance(result, tuple):
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}\nNumber of rabbits: {rabbits}")
else:
    print(result)


#4
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    return list(filter(prime, numbers))

#Usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers_list)
print(numbers_list) #original list
print(prime_numbers) #prime numbers


#5
from itertools import permutations
def print_permutations(input_string):
    permuted_strings = permutations(input_string)
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))

#Usage:
user_input = input("Enter a string: ")
print_permutations(user_input) #all permutatiations of the string



#6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#Usage:
user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Reversed sentence:", result)




#7
def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#Usage
print(has_33([1, 3, 3]))   # True
print(has_33([1, 3, 1, 3]))    #False
print(has_33([3, 1, 3]))     #False


#8
def spy_game(nums):
    index_0 = index_1 = index_2 = float('inf')
    for i, num in enumerate(nums):
        if num == 0:
            index_0 = i
        elif num == 7:
            if i > index_1 > index_0:
                index_2 = i
    return index_0 < index_1 < index_2

#Usage:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  #True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))    #True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))     #False


#9
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

#Usage:
radius = float(input()) #radius of the sphere 
result = sphere_volume(radius)
print(f{radius}, {result:.2f}) #the volume of the sphere with radius



#10
def unique_el(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#Usage:
original_list = [1, 2, 3, 1, 2, 4, 5, 6, 4]
result = unique_el(original_list)
print(original_list)
print(result) #list with the unique elements 



#11
def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

#Usage:
user_input = input() #word or phrase 
if is_palindrome(user_input):
    print(f{user_input}) #palindrome
else:
    print(f{user_input}) #not palindrom



#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#Usage:
histogram([4, 9, 7])


#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    user_name = input()
    print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        user_guess = int(input())
        guesses_taken += 1
        if user_guess < secret_number:
            print("Your guess is too low.")
        elif user_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {user_name}! You guessed my number in {guesses_taken} guesses!")
            break

# Run the game
guess_the_number()