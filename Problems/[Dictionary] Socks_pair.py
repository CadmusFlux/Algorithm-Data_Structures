#There is a large pile of socks that must be paired by color. 
#Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.


def sockMerchant(n, ar):
    dict1 = {}
    
    for i in range(n):
        
        stri = str(ar[i])
        if stri in dict1.keys():
            dict1[stri] += 1
        else:
            dict1[stri] = 1
            
    pairs = 0
    
    for j in dict1:
        
        pairs += dict1[j]//2
     
    return pairs

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
