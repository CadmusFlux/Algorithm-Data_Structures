Problem Statement :

                  Given: an array containing hashes of names

                  Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
                  
                  namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
                  # returns 'Bart, Lisa & Maggie'

                  namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
                  # returns 'Bart & Lisa'

                  namelist([ {'name': 'Bart'} ])
                  # returns 'Bart'

                  namelist([])
                  # returns ''
                  
Code : 
        
                  def namelist(names):
                  
                    length = len(names)

                    if length == 0:
                      return ""

                    elif length == 1:
                      return names[0]['name']

                    else:
                      return ", ".join(name['name'] for name in names[:-1]) + " & " + str(names[-1]['name'])
