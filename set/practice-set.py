import pandas as pd
import os

# ============================= Task 1 ============================= #
data1 = {
    "Date": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop"],
    "Units_Sold": [5, 20, 15, 7, 3],
    "Unit_Price": [800, 20, 30, 150, 800],
    "Total_Sales": [4000, 400, 450, 1050, 2400]
}

data2 = {
    "Date": ["2024-07-06", "2024-07-07", "2024-07-08", "2024-07-09", "2024-07-10"],
    "Product": ["Tablet", "Mouse", "Monitor", "Keyboard", "Tablet"],
    "Units_Sold": [8, 15, 10, 12, 6],
    "Unit_Price": [300, 22, 140, 28, 300],
    "Total_Sales": [2400, 330, 1400, 336, 1800],
    "Quality": ["High", "Medium", "Low", "High", "Medium"],
}

# df = pd.DataFrame(data1)
# df = pd.DataFrame(data2)
# print(df)

# with open("set/fold/sales_data2.csv", 'w') as f:
#     df.to_csv(f, index=False)


# read
df1 = pd.read_csv("set/fold/sales_data2.csv")
# print(df)
# print("==============================")
df2 = pd.read_csv("set/fold/sales_data1.csv")
# print(df)



# combining data sets #
# combined_data = pd.concat([df1, df2], ignore_index=True)

# df = pd.DataFrame(combined_data)

# df['Region'] = ["East", "North", "West", "North", "South",
#                 "South", "West", "South", "East", "South"] 

# with open("set/fold/h1_sales.csv", 'w') as f:
#     df.to_csv(f, index=False)
#     print("Combined data written to CSV file.")

# print(combined_data)

df = pd.read_csv("set/fold/h1_sales.csv")
# print(df)



# ============================= Task 2 ============================= #
# data = {
#     "CustomerId": [1001, 1002, 1003, 1004, 1005],
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
#     "Email": ["alice.johnson@example.com", "bob.smith@example.com", "carol.white@example.com", "david.lee@example.com", "emma.wilson@example.com"],
#     "SignupDate": ["2024-01-15", "2024-02-20", "2024-03-05", "2024-04-10", "2024-05-25"],
#     "LastLogin": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
#     "Status": ["Active", "Inactive", "Active", "Active", "Inactive"],
#     "LoyaltyPoints": [120, 80, 150, 200, 60]
# }

# df = pd.DataFrame(data)

# df.to_csv("set/fold/customer_data.csv", index=False)
# # print(df)

# dataa = df.drop(columns=['region'])
# dataaa = df[df['Status'] == 'Active']
# print(dataa) 
# print('===============================')
# print(dataaa)


#  =============================== TASK 3 ============================= #

df["Quatity"] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
df.drop(columns=['region'], inplace=True)

df['Total Amount'] = df['Quatity'] * df['Unit_Price']


df['HighValue'] = df['Total Amount'] > 1000
print(df)

with open("set/fold/h1_sales_updated.csv", 'w') as f:
    df = pd.DataFrame(df)
    df.to_csv(f, index=False)
    print("Updated data written to CSV file.")