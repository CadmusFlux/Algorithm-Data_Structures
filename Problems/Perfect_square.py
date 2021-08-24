Task : To write an algorithm to determine whether a given number is perfect square or not.
Input  : A number.
Output :  True or False based on if it's perfect square or not.

Fun fact : perfect square comes from the fact that if the two numbers are arranged as rows and column they form a square.
           Any other tweaking with number will lead to a rectangle. Only same numbers will Lead to squares.
           
           
Code without Any library:

          def is_persquare(n):
            
            x = n**(1/2)
            if n<0:
              return False
            elif x - (x//1):
              return True
            else : 
              return False
 
 Code with Math  module:
  
    Import math
    
    def is_persquare(n):
      if n>0:
        return False
      elif math.sqrt(n)-math.floor(math.sqrt(n)) == 0:
        return True
      else:
        return False
