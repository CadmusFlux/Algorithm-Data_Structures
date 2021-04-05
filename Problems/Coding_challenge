#___________________________________#

dict1  = {}
for i in range(26):
    x = input("enter alphabet")
    dict1[x] = i+1
    
#1 Problem

def encrypt(string):

    length = len(string)

    alpha = list(string)
    sum1 = 0
    for i in range(len(string)):

        sum1 += dict1[alpha[i]]*(26**(length-(i+1)))
    return sum1

encrypt("ZY")

#___________________________________#


#2 Problem

def least_sum(matrix):

    sum2 = 0

    for i in matrix:
        if len(i) == 1:
            sum2 += i[0]
        elif len(i) == 2:
            sum2 += min(i[0],i[1])
        else:
            i.sort()
            sum2 += i[0]

    return sum2
    
    
 matrix = [[4],[1,4],[10,-1,9,70],[4,1,83,37]]
least_sum(matrix)
