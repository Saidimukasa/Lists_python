students=['Saidi','Timothy','Samson','Baker']
students[2]="Samuel"#This is how to change the value of a list since lists are Mutable
print(students[2])#This is how to access a single element from the list
#Changing the Range of the list
students[0:2]=['Saidi','Timothy']#This is how to change the range of the list
#Inserting a new element into the list
#insert Method("Index","Value")
students.insert(4,"Kamulegeya")#This is how to insert a new element into the list
#But this bases on the index number provided
print(students)
#Adding a new element to the list
#Append is used to add a new element to the list but this is placed at the End of the list
#append() is a method that is used to add a new element to the list
students.append("Ddembe")#This is how to add a new element to the list
#The append method takes exactly one argument per call
students.append("Kibalama")
print(students)

#Extend Method("List")
#Extend Method this is used to append elements from another list to the current list
#Extend Method takes exactly one argument per call
tropical=['Mango','Pineapple','Banana']
students.extend(tropical)#This is how to add elements from another list to the current list
print(students)
#This elements Added using the Extend Method are added at the end of the list
#You can also add iterables to the list such strings and tuples
colors=('Red','Blue','Green')#This is Tuple
students.extend(colors)#This is how we can also added a tuple to the list
print(students)

#Removing items from the list
#Remove Method("Value") Syntax
students.remove("Saidi")#This is how to remove an element from the list
#The remove menthod takes exactly one argument per call
print(students)

#OR One can use the POP Method But this removes the Element at a given index
#POP Method("Index") Syntax LISTNAME.POP("Index")
students.pop(3)#This is how to remove an element from the list
print(students)
print(len(students))#This is how to get the length of the list
#The len() function is used to get the length of the list

#Del keyword this is used to remove an element from the list basing on the index
Fruits=['Mango','Pineapple','Banana','Orange','Apple']
del Fruits[2]#This is how to remove an element from the list
print(Fruits)
#The del can also delete the entire list
# del Fruits#This is how to delete the entire list
print(Fruits)#This will give an error since the list has been deleted
 
 
 #Clear Method this is used to empty the list but the lis remains
 #Clear Method Syntax LISTNAME.CLEAR()
Delicacies=['Mango','Pineapple','Banana','Orange','Apple']
Delicacies.clear()#This is how to clear the list
print(Delicacies)#This will print an empty list

#Looping through the list
#You can loop through the list using the for loop
#For loop Syntax
for x in students:
    print(x)#This is how to loop through the list
    
    #or
for x in students:
    for y in Fruits:
        print(x,y)#This is how to loop through the list when you have two lists
        #For this case you need to use two for loops or Nested for loops loops
   
   #Looping using the len() function
for x in range(len(students)):
       print(students[x])#This is how to loop through the list using the len() function
       #In the print statement you need to use the index number of the list
#You can use the range() function to specify the range of the list and the Len() function to get the length of the list

#Using len() function and range() function to loop through the list for more than one list
for x in range(len(students)): #This is going to loop through the students list to make a matrix kind of thing
     for y in range(len(Fruits)):
         print(students[x],Fruits[y])#This is how to loop through the list using the len() function
         #In the print statement you need to use the index number of the list

#Using the While loop to loop through the list
#While loop Syntax
students=['Saidi','Timothy','Samson','Baker']
i=0
while i < len(students):#For this case you need to use the len() function to get the length of the list
     print(students[i])
     i+=1#This is how to loop through the list using the while loop
     #In the print statement you need to use the index number of the list
     
#SORTING THE LIST
#Sort Method Syntax LISTNAME.SORT()
students=['Saidi','Timothy','Samson','Baker']
#Sort Method this is used to sort the list in ascending order or alphabetical order
students.sort()#This is how to sort the list
print(students)
ages=[12,34,56,78,90,23,45,67,89,10]
ages.sort()#This is how to sort the list
print(ages)#The list ages is sorted in ascending order or from the smallest to the largest

#Sort descending order
#Sort Method Syntax LISTNAME.SORT(reverse=True)
students=['Saidi','Timothy','Samson','Baker']
students.sort(reverse=True)#This is how to sort the list in descending order
 #We use the True keyword to sort the list in descending order
print(students)

#Reverse Order
#This is used to reverse the order of the list but this does not sort the list
#Reverse Method Syntax LISTNAME.REVERSE()
students.reverse()#This is how to reverse the order of the list
print(students)


#Copy Method this is used to copy the list
#This limits repetition of the list
students=['Saidi','Timothy','Samson','Baker']
lectures=students.copy()#This is how to copy the list
print(lectures)


#Joining two lists
#Join Method this is used to join the list
#There are very many ways to join the list the Easiest way is to use the + operator
 #Join Method Syntax LISTNAME1+LISTNAME2
list1=['Saidi','Timothy','Samson','Baker']
list2=['Mango','Pineapple','Banana','Orange','Apple']
list3=list1+list2#This is how to join the list
print(list3)
#Another way to join the list is to use the extend method()
list1.extend(list2)
print(list1)#This also another way to join a list
 