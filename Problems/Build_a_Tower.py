#Build #a #Tower

Build a Tower using asterik symbol "*" .
Input :  Number of floors will be passed as an argument.
Ouput :  Print a formatted list with each list item having the same number of elements. Fill the non-asterik Places with spaces.

Sample Input and Output : tower_builder(4) : ['   *   ', '  ***  ', ' ***** ', '*******']

Intital code: 
    
    def tower_builder(n_floors):
      lists = []
      for i in range(n_floors):
          spaces = " "*(n_floors-(i+1))
          strings = "*"*2*(i) + 1
          a = spaces+strings+spaces
          lists.append(a)

      return lists
      
Refactored-code :
              
    def tower_builder(n_floors):
      lists = [" "*(n_floors-(i+1))+"*"*(2*(i) + 1)+" "*(n_floors-(i+1)) for i in range(n_floors)]
      return lists
