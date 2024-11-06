# Python code to demonstrate the use of default arguments    
# defining a function    
def function( n1, n2 = 20 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
       
# Calling the function and passing only one argument    
print( "Passing only one argument" )    
function(30)    
    
# Now giving two arguments to the function    
print( "Passing two arguments" )    
function(50,30)

print("----------------------------------------------------------------")

# Python code to demonstrate the use of keyword arguments    
  # Defining a function    
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
# Calling function and passing arguments without using keyword    
print( "Without using keyword" )    
function( 50, 30)       
        
# Calling function and passing arguments using keyword    
print( "With using keyword" )    
function( n2 = 50, n1 = 30)

print("-------------------------------------------------------------")

# Python code to demonstrate the use of default arguments      
# Defining a function    
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30    
print( "Passing out of order arguments" )    
function( 30, 20 )       
    
# Calling function and passing only one argument    
print( "Passing only one argument" )    
try:    
    function( 30 )    
except:    
    print( "Function needs two positional arguments" )  

print("------------------------------------------------------------")

# Python code to demonstrate the use of variable-length arguments       
# Defining a function    
def function( *args_list ):    
    ans = []    
    for l in args_list:    
        ans.append( l.upper() )    
    return ans    
# Passing args arguments    
object = function('Python', 'Functions', 'tutorial')    
print( object )    
    
# defining a function    
def function( **kargs_list ):    
    ans = []    
    for key, value in kargs_list.items():    
        ans.append([key, value])    
    return ans    
# Paasing kwargs arguments    
object = function(First = "Python", Second = "Functions", Third = "Tutorial")    
print(object)

print("----------------------------------------------------------------")

# Python code to demonstrate the use of return statements      
# Defining a function with return statement    
def square( num ):    
    return num**2    
     
# Calling function and passing arguments.    
print( "With return statement" )    
print( square( 52 ) )    
    
# Defining a function without return statement     
def square( num ):    
     num**2     
    
# Calling function and passing arguments.    
print( "Without return statement" )    
print( square( 52 ) )    

print("----------------------------------------------------------")

























