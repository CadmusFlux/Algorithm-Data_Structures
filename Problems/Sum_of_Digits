Simplified-Problem : # Keep adding the digits of the input until the sum is a single digit.

Input : Any integer
Output : Single Digit


Code:

    def digits_sum(n):
  
        list = [int(x) for x in str(n)]
        if len(list) == 1:
          return n
        else : 
          sum = 0
          for i in list:
            sum += i  
          n = sum
          return digits_sum(n)
