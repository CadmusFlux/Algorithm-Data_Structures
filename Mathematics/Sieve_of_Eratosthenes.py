# Mathematical theory :- [https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes]

import math
import numpy as np

x = np.arange(2,1000,1,int)

i = 0

while i != len(x):

    curr_num = x[i]
    # print("\n Start: \n")
    # print("curr_num",curr_num)

    for j in range(i+1,len(x)):

        if x[j] % curr_num == 0:

            x[j] = 0
    
    # print("Updated list",x)

    value = x[i]
    for index in range(i+1,len(x)):

        if 0 < x[index] < 50:
            i = index
            break
    
    if value == x[i]:
        break
    
prime_numbers = list(filter(lambda n : n != 0,x))

print(prime_numbers)
