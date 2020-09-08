Problem Statement : 
                  Take a number and sum it's consecutive digits with consecutive powers . Return the numbers whose  sum is equal to the original number. 
                   
Input :  Range : (a,b)
Output : List with numbers satisfying the condition.

For e.g :  1) 89 = 8^1 + 9^2    2) 135 = 1^1 + 3^2 + 5^3
                 = 8+81                = 1+9+125
                 = 89                  = 135
                 
Code : 
    
      def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    
          z = []
          for i in range(a,b+1):
              x = [ ]
              sum = 0 
              [x.append(int(d)) for d in str(i)] 
              for j in range(len(x)):
                sum += x[j]**(j+1)
              if sum == i:
                z.append(i)

          return z
          
Ideal : 
        def filter_func(a):
          return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

        def sum_dig_pow(a, b):
          return filter(filter_func, range(a, b+1))
    
