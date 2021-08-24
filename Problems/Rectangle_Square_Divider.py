Problem Statement:

          You will be given length and width of a rectangle , return the squares that can be built inside it.
          link: [https://www.codewars.com/kata/55466989aeecab5aac00003e/python]


Solution:

          def sqInRect(lng, wdth):

              list1= []
              i = lng
              j = wdth

              while True:

                  if i<j:
                      j = j-i
                      list1.append(i)
                  elif j<i :
                      i = i-j
                      list1.append(j)
                  else:
                      if len(list1)<1:
                          return None
                      else:
                          list1.append(i)
                          break

                  # print(i,j)
              return list1
