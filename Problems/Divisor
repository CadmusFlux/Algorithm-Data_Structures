'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math

test_cases = int(input())
numbers = []
for i in range(test_cases):
    numbers.append(int(input()))

for j in range(len(numbers)):
    divisors = [1]
    for k in range(2,math.ceil(math.sqrt(numbers[j]))):
        if numbers[j] % k == 0:
            divisors.extend([k,numbers[j]//k])
    if sum(divisors) == numbers[j]:
        print("YES")
    else:
        print("NO")


