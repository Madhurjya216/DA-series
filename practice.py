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
import csv

data = [
    [1, "Raj", 21, 98],
    [2, "Rahul", 41, 95],
    [3, "Ram", 23, 97],
    [4, "Raja", 24, 91],
    [5, "Rani", 25, 99],
    [6, "Rita", 26, 96],
    [7, "Ravi", 27, 94],
    [8, "Rohan", 28, 93],
    [9, "Riya", 29, 92],
    [10, "Rohit", 30, 90],
    [11, "Rashmi", 31, 89],
    [12, "Rajesh", 32, 88],
    [13, "Rakesh", 33, 87],
    [14, "Rupal", 34, 86],
    [15, "Ruchi", 35, 85]
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
import pandas as pd
import os


# writing to file 
# with open("fold/newData.csv", 'w') as f:
#     df = pd.DataFrame(data, columns=columns)
#     df.to_csv(f, index=False)
#     print("Data written to CSV file using Pandas.")



#  reading csv file
with open("fold/pdData.csv", 'r') as f:
    df = pd.read_csv(f)
    # print(df.fillna("Ravi"))  



 

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



df = pd.read_csv("fold/pdData.csv")
df.dropna(inplace=True)  # removes rows with any NaN values
df['Total'] = df['Age'] + df['Salary']  # adding
print(df)

