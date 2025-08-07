import pandas as pd
import os
import csv
import json



# to create data
# data = [
#     ["ID", "NAME", "Roll No.", "Marks"]
#     [001, "Raj", "21", 98]
#     [002, "Rahul", "41", 95]
#     [003, "Ram", "23", 97]
#     [004, "Raja", "24", 91]
# ]


# data = ["This is the plain text file!",
#         "\nThis is the second line of the file.",
#         "\nThis is the third line of the file."]


# with open("fold/mypata.txt", 'w') as f:
#     f.write(data)
    # print("done!")

# with open("fold/mypata.txt", 'x') as f:
#     f.writelines(data)
#     print("done!")


# Reading text file #
# with open("fold/myData.txt", 'r') as f:
#     content = f.read()
#     print(content)

# with open("fold/myData.txt", 'r') as f:
#     content = f.readlines()
#     print(content)

#  ======= CSV code ======= #

data = [
    [101, "Raj", 21, 98],
    [102, "Rahul", 41, 95],
    [103, "Ram", 23, 97],
    [104, "Raja", 24, 91],
    [105, "Rani", 25, 99],
    [106, "Ravi", 26, 96]
]

columns = ["ID", "NAME", "Roll No.", "Marks"]

# Writing CSV file #
# with open("fold/myData.csv", 'w') as f:
#     write = csv.writer(f)
#     write.writerows(data)
#     print("Writing data to CSV file...")

# with open("fold/myData.csv", 'a') as f:
#     write = csv.writer(f)
#     write.writerows(data)
#     print("Appending data to CSV file...")



# with open("fold/myData.csv", 'r') as f:
#     read = csv.reader(f)
#     for i in read:
#         print(i)




# ========= PANDAS ========= #



# writing to file 
# with open("fold/pdData_UI.csv", 'a') as f:
#     df = pd.DataFrame(data, columns=columns)
#     df.to_csv(f, index=False)
#     print("Data written to CSV file using Pandas.")



# Create a DataFrame with date strings
# df = pd.DataFrame({'date': ['2024-01-01', '2024-02-15', '2024-03-10', '2024-04-05',
#                             '2024-05-20', '2024-06-30']})

# df['date'] = pd.to_datetime(df['date'])
# df['year'] = df['date'].dt.year
# df['month'] = df['date'].dt.month
# print(df)

#  reading csv file
# with open("fold/pdData.csv", 'r') as f:
#     df = pd.read_csv(f)
    # print(df.fillna("Ravi"))  


# with open("fold/pdData_UI.csv", 'r') as f:
    # df = pd.read_csv(f)
    # print(df)
 

# with open("fold/newData.csv", 'a') as f:
#     df = pd.DataFrame(data)
#     df.to_csv(f, header=False, index=False)
#     print("Data appended to CSV file using Pandas.")



#============ delete file  =============#
# os.remove("fold/newData.csv")
# print("File deleted successfully.")


#  ========== SORTING DATA ========== #
# con = df.sort_values(by="Salary", ascending=False)
# print(con)


# ============ Adding Calculated Columns ============ #
# df['Total'] = df['Age'] + df['Salary']
# print(df)


# df.dropna(inplace=True)  # removes rows with any NaN values
# print(df) 

# print(df.describe())  # prints summary statistics of the DataFrame



# df = pd.read_csv("fold/pdData_UI.csv")
# df.dropna(inplace=True)  # removes rows with any NaN values
# # df['Total'] = df['Age'] + df['Salary']  # adding
# print(df)


# ===== drop entire file ========= #
# os.remove("fold/pdData_UI.csv")
# print("done!")


#  ========== file joining securely ========== #
# file_path = os.path.join("fold", "data.txt")  # Joins folder and file name safely
# df = pd.read_csv(file_path)  # Reads the CSV using the safe path
# print(df)  # Displays the DataFrame 



# ===================================== JSON file handling - pandas =========================================== #

    # data = [
    # {"name": "Alice", "age": 25, "city": "Delhi"},
    # {"name": "Bob", "age": 30, "city": "Mumbai"}
    # ]


    # with open("fold/data.json", "w") as f:
    #     json.dump(data, f, indent=4)
    #     print("done!")



    # with open("fold/data.json") as f:
    #     data = json.load(f)
    #     print(data)

