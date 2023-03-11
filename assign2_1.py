list1= input('Enter a set of numbers: ').split(' ')
list2= [] #int to be added
#print(list1) #input number as strings
for i in list1:
    list2.append(int(i))

#print(list2) #strings to integers
#print(len(list2))
list3=[]  #tuple to be added 
for j in range(0,len(list2)-1):
    if j == len(list2):
       break
    else:
        tup= ((list2[j]),(list2[j+1]))
        #print(tup)        
    list3.append(tup)
    
print(list3)

list4 =[(i[-1],i) for i in list3] # last element of each tuple
    
#print(list4)
(list4.sort())
#print(list4)
list5= [(i[1]) for i in list4] # sorted tuple by last element of each tuple in a list
print(list5)