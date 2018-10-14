#a)
values = [3,2,5,6,-7]
squared_list = []
display_list = []
print('Regular list: ', values)
         
squared_list = [i**2 for i in values]
for i in range(0,len(squared_list)):
    squared_str = str(squared_list[i])
    display_string = 'y*y = ' + squared_str
    display_list.append(display_string)
print('Squared list version 1: ', display_list, '\n')



#b)
display_list = []
#squared_list stays the same
for i in range(0,len(values)):
    squared_str = str(squared_list[i])
    index_str = str(i + 1)
    display_string = 'solution #'+ index_str + ' = ' + squared_str
    display_list.append(display_string)
print('Regular list: ', values)
print('Squared list version 2: ', display_list, '\n')
    
#c)
lst = ['zero','one','two','three']
tuple_lst = [(i,lst[i]) for i in range(0,len(lst))]
        
print('Tuple list: ', tuple_lst, '\n')
        
#d)

lst1 = ['j', 'q', 'p']
lst2 = [4,6]
lst3 = [(lst1[i],lst2[j]) for i in range(0,len(lst1)) for j in range(0,len(lst2))]                            
        
print('Cartesian Product list: ', lst3, '\n')
    
#e)

lst1=[56,25,8,11,16,20,18,50,7,42]
lst2 =[5,3,6]
lst3 = []
for i in range(0, len(lst1)):
    for j in range(0,len(lst2)):
        if lst1[i] % lst2[j] == 0:
            lst3.append(lst1[i])
            

print('Common divisor list: ', lst3)

