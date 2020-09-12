Statement :  Write an algorithm to number each element of a list in ascending order.

Input : List with somw characters.

Output : List with enumareted string values.

Code : 
      def number(lines):
          for i in range(len(lines)):
            lines[i] = str(i+1)+": "+lines[i]
          return lines
          
Refactored Code : 

      def number(lines):
          return [str(x+1) + ": " + lines[x] for x in range(len(lines))]
