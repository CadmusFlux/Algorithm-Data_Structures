Simpified Version : Remove certain set of characted if encountered in a string and replace it with a string:
                    1) If the substring(set of character) are at start or end do not replace with space.
                    2) If substring is encountered consecutively replace by just a single string.
                   
Input :  String with substring ("WUBHeyWUBIWUBamCadmusFluxWUB")
Output:  Edited string with substring removed. ("Hey I am CadmusFlux")

Initial Solution : 

                  def polycarpus(song):

                    for i in range(len(song)):

                      if i==len(song):
                        break
                      elif i>len(song):
                        break
                      elif song[i]=="W" and song[i+1] =="U" and song[i+2]=="B" :
                        if i == 0:
                          song = song[i+3:]
                        elif i+2 == len(song)-1:
                          song = song[:i]
                        else:
                          song = song[:i]+str(" ")+song[i+3:]

                    song = " ".join(song.split())  
                    return song
Simplified solution: 
                    def polycarpus(song):
                     
                      return " ".join((string.replace("WUB"," ")).split()) 
