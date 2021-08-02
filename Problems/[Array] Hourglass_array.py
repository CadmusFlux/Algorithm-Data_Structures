# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# ----------- Input ------------
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

# ----------- CODE ------------

def hourglassSum(arr):
    
    maximum = 0
    flag = 0
    
    for i in range(len(arr[0])):
        for j in range(len(arr[1])):
            
            if i not in [4,5] and j not in [0,5]:
                
                sum = arr[i][j]+arr[i][j-1]+arr[i][j+1]+arr[i+2][j-1]+arr[i+1][j]+arr[i+2][j+1]+arr[i+2][j]
                
                if flag == 0:
                    maximum = sum
                    flag = 1
                if sum >= maximum:
                    maximum = sum
                    
    return maximum
