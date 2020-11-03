Problem Statement : 
                    Chef calls a sequence good if it does not contain any two adjacent identical elements.

                    Initially, Chef has a sequence a1,a2,…,aN
                    . He likes to change the sequence every now and then. You should process Q queries. In each query, Chef chooses an index x and changes the x-th element of the sequence to y

                    . After each query, can you find the length of the longest good subsequence of the current sequence?

                    Note that the queries are not independent.
                    
Code : 

        class Node:
     
             def __init__(self,pre_value):
                 self.pre_value = pre_value
                 self.post_value = self.pre_value
                 self.next = None

        class Llist:

            def __init__(self):
                self.head = None

            def list_Llist(self,list):

                for i in range(len(list)):

                  new_node = Node(list[i])

                  if self.head is None:
                    self.head = new_node
                  else:
                    temp = self.head
                    while temp.next != None:
                      temp = temp.next
                    temp.next = new_node

            def change(self,index,new_value):
              count = 0
              temp = self.head
              while temp != None and count < index:
                temp = temp.next
                count += 1
              temp.post_value = new_value

            def compare(self):
              count = 0
              max = 0
              temp = self.head
              while temp != None:

                if temp.pre_value == temp.post_value:
                  temp = temp.next
                  count += 1
                else :
                  temp = temp.next
                  if count > max :
                    max = count
                  count = 0

              return max

            def reset(self):
              temp = self.head
              while temp != None:
                if temp.pre_value != temp.post_value:
                  temp.post_value = temp.pre_value
                temp = temp.next



            def display(self):

              temp = self.head

              while temp != None:
                print([temp.pre_value,temp.post_value])
                temp = temp.next


        sll = Llist()
        list1 = [1,3,4,2,6,7]
        sll.list_Llist(list1)
        sll.change(3,9)
        sll.display()
        print(sll.compare())
        sll.reset()
        sll.display()
