# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#
#  Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.

#---------- Cloud ----------

def jumpingOnClouds(c):
    
    i = 0
    jumps = 0
    
    while i+2 < len(c):
        
        if c[i+2]== 0:
            i += 2
            jumps += 1
        else:
            i+= 1    
            jumps += 1
    
    if i != len(c)-1:
        jumps += 1
        
    
    return jumps

if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

