Problem Statement : Fibonacci product . A number will be passed as an argument and you have to write a algorithm to print the factors which have to be consecutive fibonacci
                    numbers. The second to print along with the factor is a boolean value. So if the input has factors in the fibonacci series then return True . If the there 
                    are no valid factors than return the smallest fibonacci number which when multipled to the next number has product greater than the input along with boolean
                    False.

Input : Number (prod)

Output : [num1,num2,True/False] , A list with the two factors and the boolean value.

Code : 

      def fibonacci(n):
        x = 0
        y = 1
        sum = 0
        for i in range(2,n+2):
            x0 = sum
            sum = x+y
            x = y
            y = sum
        return x0,sum

     def productFib(prod):
        i = 2
        if prod == 0:
            return [0, 1, True]
        elif prod == 1:
            return [1, 1, True]
        while i > 0:
            x1,x2 = fibonacci(i)
            if x1*x2 == prod:
                return [x1,x2,True]
            elif x1*x2>prod:
                return [x1,x2,False]
            i = i+1
