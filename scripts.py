# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")
  

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
First_result = a + b 
print (First_result)

Second_result = a - b
print(Second_result)

Third_result = a * b
print(Third_result)


# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
First_result = a//b
print(First_result)

Second_result =a/b
print(Second_result)


# Loops
if __name__ == '__main__':
    n = int(input())
if n > 0:
    for i in range(n):
        print(i**2)

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
result = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if i + j + k != n] 
print (result)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)
arr.sort()
max_result = arr[-1]    
for i in range(n - 1, -1, -1):
    if arr[i] < max_result:
        print(arr[i])
        break

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

scores = student_marks[query_name]       
avarage = sum(scores) / len(scores)
print(f"{avarage:.2f}")


# Lists
if __name__ == '__main__':
    N = int(input())
    my_list = []
    
for _ in range(N):
    command = input().split()
    action = command[0]
    
    if action == 'insert':
        my_list.insert(int(command[1]), int(command[2]))
    elif action == 'print':
        print(my_list)

    elif action == 'remove':
        my_list.remove(int(command[1]))
    
    elif action == 'append':
        my_list.append(int(command[1]))
    
    elif action == 'sort':
        my_list.sort()
        
    elif action == 'pop':
        my_list.pop()
        
    elif action == 'reverse':
        my_list.reverse()


# Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())    

t =tuple(integer_list)
print(hash(t))

# Nested Lists
if __name__ == '__main__':
    python_students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])

Voti =[]
for studente in python_students:
    Voti.append(studente[1])
    
Voti.sort()
lowest = Voti[0]
for i in Voti:
    if lowest != i:
        second_lowest = i
        break

group = []
for i in python_students:
    if i[1] == second_lowest:
        group.append(i[0])
        
group.sort()    
for i in group:
    print(i)    
        
# What's Your Name?
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here

    print("Hello ", end ="")
    print (first_name, last_name, sep =' ', end ="")
    print("! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# String Split and Join
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    result = "-".join(line)
    return result
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Mutations
def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    string = ''.join(string_list)   
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string
def count_substring(string, sub_string):
    
    count = 0
    count_substring = len(sub_string)
    for i in range (len(string)):
        if string[i:count_substring + i] == sub_string:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



# Text Wrap
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Introduction to Sets
def average(array):
    # your code goes here
    heights = set(array)
    avg = sum(heights)/ len(heights)
    return round(avg, 3)  

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT

dimensione_M = input()
M = input()
lis_M = M.split()
set_M = set(map(int, lis_M))

dimensione_N = input()

N = input()
lis_N = N.split()
set_N = set(map(int, lis_N))

result = sorted(set_M.symmetric_difference(set_N))

for i in result:
    print(i)



# Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.


def birthdayCakeCandles(candles):
    # Write your code here

    max_height = max(candles)
    return candles.count(max_height)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
