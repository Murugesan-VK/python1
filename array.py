#Simple Array

import array as arr  
a = arr.array('i', [2, 4, 6, 8])  
print("First element:", a[0])  
print("Second element:", a[1])  
print("Second last element:", a[-2])   
print("-------------------------------------------------------------------")

import array as arr  
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  

print(numbers)
# changing first element  
numbers[0] = 10     
print(numbers) # Output: array('i', [10, 2, 3, 5, 7, 10])  
   
# changing 3rd to 5th element  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)   # Output: array('i', [10, 2, 4, 6, 8, 10])
print("------------------------------------------------------------------")

#Array Concatenation
import array as arr  
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])  
b=arr.array('d',[3.7,8.6])  
c=arr.array('d')  
c=a+b  
print("Array c = ",c)
print("-------------------------------------------------------------")



















