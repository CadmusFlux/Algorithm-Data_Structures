# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#
#----- CODE ------

def repeatedString(s, n):
    
    l1 = 0
    
    for i in s:
        
        if i == "a":
            l1 += 1
    
    length = len(s)
    repeat = n // length
    remainder = n % length
    frequency = repeat*l1
    
    i =0 
    while i<remainder:
         if s[i] == "a":
            frequency += 1
         i += 1
    
    return frequency
        

if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
