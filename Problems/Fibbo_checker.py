import math

def Square_checker(x):
    s = int(math.sqrt(x))
    return s*s == x

def fibo(n):
 
    return Square_checker(5*n*n + 4) or Square_checker(5*n*n - 4)

def myfunc(numbers):

    for i in numbers:
        if fibo(n)
            print(n)
        else:
 
        fibo1 = 0
        fibo2 = 2
        sum = fibo1 + fibo2
     
        while (fibo2 <= n) :
    
            curr = 4 * fibo2 + fibo1

            if (curr > n) :
                break

            fibo1 = fibo2
            fibo2 = curr
            sum = sum + fibo2
        
        return sum
