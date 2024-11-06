'''
# Creating a dictionary
my_dict = {
    "name": "Prakash",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair
my_dict["gender"] = "Male"

# Modifying a value
my_dict["age"] = 32

# Removing a key-value pair
del my_dict["city"]

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, ":", value)
'''
days_in_month={
    'january':31,
    'february':28,
    'march':31,
    'april':30,
    'may':31,
    'june':30,
    'july':31,
    'august':31,
    'september':30,
    'october':31,
    'november':30,
    'december':31
    }
month=input("Enter the Month(e.g January,February):").lower()
if month in days_in_month:
    if month=='february':
        a=int(input("Enter the Year:"))
        if a%4==0:
            print("There are 29 Days in February")
        else:
            print("There are 28 Days in February")
    else:
        num=days_in_month[month]
        print("There are",num,"Days in Month")
else:
    print("invalid input")
    




































