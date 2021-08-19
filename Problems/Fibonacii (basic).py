Note : In common nth term fibonacci problems you will encounter that often zero is omitted.  So the index starts from 1 as usual. So say for example 8th term will be 21 
       according to both indexing method . No need to apply (0,n-1) logic here.
       
code : 
      def fibo(n):
        x = 0
        y = 1
        sum = 0
        for i in range(2,n):
          sum = x+y
          x = y
          y = sum

        return sum
