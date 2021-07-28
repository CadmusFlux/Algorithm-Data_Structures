# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
#
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 

# -------- CODE ------------


def countingValleys(steps, path):
    
    level = 0 
    valley = 0
    
    for i in range(steps):
         
        prev_level = level
        
        if path[i] == 'U':
            level += 1
        else:
            level -= 1
        
        if level ==-1 and prev_level == 0:
            
            valley += 1
            
    return valley

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

