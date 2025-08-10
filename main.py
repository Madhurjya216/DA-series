import pandas as pd



# a = 65342
# print(a)


# str = 'this is string'
# print(str)

# flt = 3.14159
# print(flt)

# bool = False
# print(bool)

# type casting #
# b = 212
# c = str(b)
# print(type(c))

# data structures - List #
# list = [1, 2, 3, 3, 4, 5]
# print(list[1:4])
# print(list[1:5:3])  # Slicing with step
# print(list.append(6))  # Appending to the list
# print(list.insert(5, 7))  # inserting to the list
# print(list.extend([7, 8]))  # extending a list
# # # print(list.remove(1)) # Remove first occurrence of 1
# # # print(list.pop()) # Remove last element
# # del list[0]  # Delete first element
# print(list.clear())  # Clear the list
# print(list.count(3))  # Count occurrences of 7
# print(list.index(3))  # Find index of first occurrence of 3
# print(list.reverse())  # Reverse the list   
# # print(list.sort())  # Sort the list
# print(len(list)) # Get the length of the list
# print(list)  # to display the final list


# data structures - tuple #
# tuple = (1, 2, 3, 4, 5)
# print(tuple[1:4])  # Slicing a tuple
# print(tuple[1:5:3])  # Slicing with step
# print(tuple.count(3))  # Count occurrences of 3
# print(tuple.index(3))  # Find index of first occurrence of 3
# print(len(tuple)) # Get the length of the tuple
# print(tuple + (6,7,8,9)) # Concatenate tuples
# print(tuple * 2)  # Repeat the tuple

# data structures - Dictionary #
# dic = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(dic["name"])  # Accessing value by key
# print(dic.get("age"))  # Accessing value using get method
# print(dic.keys())  # Get all keys
# print(dic.values())  # Get all values
# print(dic.items()) # Get all key-value pairs
# dic2 = dic.copy()  # Copying dictionary
# dic["country"] = "USA"  # Adding a new key-value pair
# dic["age"] = 40  # Modifying an existing key-value pair
# dic.update({"age": 45, "city": "paris"})
# print(dic.pop("city"))  # Removing a key-value pair
# print(dic.update({"country": "USA"}))  # Adding a new key-value pair
# print(dic)


# data structures - Sets #
# set1 = {1,4,7,9,3,4,5,0}
# set2 = {1,1,7,9,8,4,7,3}
# set.add(10)  # Adding an element to the set
# set.remove(12)  # Removing an element from the set
# set.discard(12)  # Discarding an element (no error if not found)
# set.update([2, 3, 5])  # Updating the set with multiple elements
# set.clear()  # Clearing the set
# set.pop()  # Removing and returning an arbitrary element from the set
# print(f"Union set: {set1 | set2}")   # Set union
# print(f"Intersection set: {set1 & set2}")   # Set intersection
# print("Difference set: ", set1 - set2)   # Set difference
# print("Symmetric difference set: ", set1 ^ set2)   # Symmetric difference


# IF-ELSE conditionals #
# x = 20
# y = 20  
 
# if x < y:
#     print(f"{x} is less than {y}")
# else:
#     print(f"{x} is greater than {y}")


# # Nested IF-ELSE conditionals #
# if x < y:
#     print(f"{x} is less than {y}")
# elif x == y:
#     print(f"{x} is equal to {y}")
# else:
#     print(f"{x} is greater than {y}")


# Ternary operator #
# result = f"{x} is less than {y}" if x < y else f"{x} is greater than {y}"
# print(result)


# Nested if-else #
# if x < y:
#     if x < 10:
#         print(f"{x} is less than 10 and also less than {y}")
#     else:
#         print(f"{x} is less than {y} but not less than 10")
# else:
#     if x == y:
#         print(f"{x} is equal to {y}")
#     else:
#         print(f"{x} is greater than {y}")



# Loops - For loop #
# num = [2,4,8,9,4,6]
# for i in range(10):
#     if i == 4:
#         continue
#     print(i)

# Loops - While loop #
# count = 100
# while count > 10:
#     if count == 50:
#         continue
#     print(count -1)
#     count -= 1

# FUNCTION #
# def greet(name):
#     print(f"Hello, {name}! This is a simple Python script demonstrating basic concepts.")

# greet("Madhurjya")

# Nested function
# def outer():
#     def inner():
#         print("Inner function")
#     inner()
#     print("Outer function")

# outer()


# lambda functions #
# add = lambda a, b, c: a+b+c
# print(add(10, 8, 9))


# Lambda functions with map
# num = 1,2,3,5,7,9
# data = map(lambda x: x, num)
# print(list(data))


# Lambda functions with filter
# num = [1,2,3,5,7,9, 10]
# data = filter(lambda x: x%2==0, num)
# print(list(data))


# Lambda functions with reduce
# from functools import reduce

# num = [2,8, 75]
# data = reduce(lambda x, y: x * y, num)
# print(data)


# file handling #
# writing file #  
# with open("data.txt", 'w') as f:
#     contain = f.write("This is a sample text file.\n")
#     print(f"Written {contain} characters to the file.")
    
# reading file #  
# with open("./fold/data.txt", 'r') as f:
#     data = f.read()
#     print(data)


# append file #
# with open("data.txt", 'a') as f:
#     data = f.write("Appending this line to the file.\n")
#     print(data)

# with open('data.txt', 'r') as f:
#     for line in f:
#         print(line.strip())


# Check for file availability #
# import os 

# if os.path.exists('data.txt'):
#     with open('data.txt', 'r') as f:
#         print("File found!")
#         print(f.read())
# else:
#     print("File does not exist.")


# Exception handling #
# import os

# file_path = os.path.join('fold', 'data.txt')
# try:
#     with open(file_path, 'r') as f:
#         print(f.read())
# except FileNotFoundError:
#     print(f"File not found: {file_path}")


# file handling using CSV module #
# import csv

# data = [
#     ["001", "Alice", 30, "New York"],
#     ["002", "Bob", 25, "Los Angeles"],
#     ["003", "Charlie", 35, "Chicago"],
#     ["004", "David", 28, "Houston"],
#     ["005", "Eve", 22, "Phoenix"]
# ]

# with open("fold/data.csv", "w", newline='') as f:
#     contain = csv.writer(f)
#     contain.writerows(data)
#     print(f"Written {len(data)} rows to the CSV file.")





# with open("fold/data.csv", "r") as f:
#     read = csv.reader(f)
#     for i in f:
#         print(i.strip())


# file handling - using pandas #



# writing to csv file
# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "madhurjya"],
#     "Age": [30, 25, 35, 28, 22],
#     "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Delhi"],
#     "Country": ["USA", "USA", "USA", "USA", "USA", "India"],
#     "Salary": [70000, 60000, 80000, 75000, 50000, 60000],
#     "Department": ["HR", "Finance", "IT", "Marketing", "Sales", "Development"],
#     "Experience": [5, 3, 7, 4, 2],
#     "Joining Date": ["2020-01-15", "2019-03-22", "2018-07-30", "2021-05-10", "2022-11-01", "2023-01-20"],
#     "Performance Score": [4.5, 3.8, 4.9, 4.2, 3.5, 4.0],
#     "Is Active": [True, True, False, True, False, True],
#     "Last Promotion Date": ["2022-06-01", "2021-08-15", "2020-12-20", "2023-02-10", "2021-09-30", "2023-03-05"],
# }


# df = pd.DataFrame(data)

# df.to_csv("fold/pdData.csv", index=False)
# print("Data written to CSV file successfully.")

# reading csv file
# df = pd.read_csv("fold/pdData.csv")
# # # print(df.info())
# # # print(df.columns)
# # # print(df.shape)
# # # print(df.describe())
# # # print(df["Salary"])
# print(df[df['Name'] == 'Alice'])



# df = pd.DataFrame(data)

# df.to_csv("fold/pdData.csv", mode='a', index=False, header=False)
# print("Data appended to CSV file successfully.")



# df = pd.read_csv("fold/pdData.csv")
# print(df)
# print(df.drop_duplicates(inplace=True))  # Remove duplicates in place
# print(df)  # This will print the DataFrame after removing duplicates

# print(df.sort_values(by='Age', ascending=True, inplace=False))

# print("done")




# ====== flltering data ====== #
# with open("fold/pdData.csv", "r") as f:
    # df = pd.read_csv(f)
    # df.drop_duplicates(inplace=True)  # Remove duplicates in place
    # print("=========================================================")
    # print(df[(df['Name'] == 'Bob')  & (df['Salary'] >= 60000)] )
    # print("=========================================================")
# 




#  ============ sorting ========= #
# con = df.sort_values(by='Salary', ascending=True)
# print(con)




#  ================= mean, mode and median =================== #
# data = {'values': [10, 20, 30, 40, 50, 50, 40 , 90, 60, 70, 60, 70, 80, 90, 100]}

# df = pd.DataFrame(data)

# mean_value = df['values']
# print(mean_value.mean())  # Calculate the mean of the 'values' column
# mode_value = df['values'].mode()
# print(mode_value)

# median_value = df['values'].median()
# df.sort_values('values', inplace=True)  # Sort the DataFrame by 'values' column
# print(median_value)



# ======= grouping data =========== #
# con = df.groupby('Name')['Age'].mean()
# print(con)

# df.drop_duplicates(inplace=True)
# con = df.groupby('Name').agg({
#     "Department": 'size',
#     "Salary": 'mean',
#     "Experience": 'sum',
# })

# print(con)

# Multiple aggregations for Salary
# print(df.groupby('Name')['Salary'].agg(['mean', 'sum', 'max']))


# df = pd.read_csv("fold/pdData.csv")
# print(df)




# ==================================== JSON DATA ========================================= #
# Example DataFrame
# df = pd.DataFrame({
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'age': [25, 30, 35],
#     'city': ['New York', 'Los Angeles', 'Chicago']
# })

# df.to_json("fold/data.json", indent=2, orient='columns')


# df = pd.read_json("fold/data.json")
# print(df)




# data = {
#   "name": "Alice",
#   "location": {
#     "city": "New York",
#     "state": "NY"
#   },
#   "pets": [
#     {"tree": "dog", "name": "Rex"},
#     {"type": "cat", "name": "Whiskers"}
#   ]
# }



nested_data = [
    {
        "id": 1,
        "name": "Alice",
        "contact": {
            "email": "alice@example.com",
            "phones": ["+1-202-555-0147", "+1-202-555-0172"]
        },
        "projects": [
            {"title": "AI Research", "budget": 50000, "team": ["Alice", "Bob"]},
            {"title": "Web App", "budget": 20000, "team": ["Alice", "Charlie"]}
        ]
    },
    {
        "id": 2,
        "name": "Bob",
        "contact": {
            "email": "bob@example.com",
            "phones": ["+1-202-555-0183"]
        },
        "projects": [
            {"title": "Cloud Migration", "budget": 75000, "team": ["Bob", "Eve"]}
        ]
    }
]


# Normalize the JSON data
df = pd.json_normalize(nested_data)
print(df)

