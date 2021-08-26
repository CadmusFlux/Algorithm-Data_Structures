Problem Statement  :  Your task, is to create NxN multiplication table, of size provided in parameter.
                      for n = 3, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
                      
Code  : 
        def multiplication_table(size):
  
          table = [[(j+1)*(i+1) for j in range(size)] for i in range(size)]
          return table
          
          
          
Refactored Code :  

        def multiplication_table(size):
  
            return [[(j+1)*(i+1) for j in range(size)] for i in range(size)]
