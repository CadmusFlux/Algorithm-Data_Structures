Problem Statement : Create ROT13 encoder. A string message will be passed as input you've to replace the alphabet with alphabet 13 ascii value ahead of it. Only aplhabets should
                    be replaced. 
                    [Fot13] (https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/ROT13_table_with_example.svg/1200px-ROT13_table_with_example.svg.png)
                    
Input : Stirng , "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

Output: String , "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

Code : 

      def rot13(string):
      
          for i in range(len(string)):
            if string[i].isalpha() and ord(string[i])>96:
              if ord(string[i]) in range(97,110):
                string = string[:i]+chr(ord(string[i])+13)+string[i+1:]
              elif ord(string[i]) in range(110,123):
                string = string[:i]+chr(ord(string[i])-13)+string[i+1:]

            elif string[i].isalpha() and ord(string[i])>64:
              if ord(string[i]) in range(65,78):
                string = string[:i]+chr(ord(string[i])+13)+string[i+1:]
              elif ord(string[i]) in range(78,91):
                string = string[:i]+chr(ord(string[i])-13)+string[i+1:]


          return string


    rot13("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")



        
