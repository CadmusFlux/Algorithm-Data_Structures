Problem Statement : Capitalize first character of each word .

Input : String

Output : Jadened string

Code : 
    
       def to_jaden_case(string):
    
          for i in range(len(string)):
              if i == 0 and string[i].islower():
                  string = string[0].upper() + string[i+1:]

              elif string[i] == " ":
                  string = string[:i+1]+string[i+1].upper()+string[i+2:]
            
          return string
