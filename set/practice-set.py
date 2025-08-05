import pandas as pd
import os

# ============================= Task 1 ============================= #
# data1 = {
#     "Date": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop"],
#     "Units_Sold": [5, 20, 15, 7, 3],
#     "Unit_Price": [800, 20, 30, 150, 800],
#     "Total_Sales": [4000, 400, 450, 1050, 2400]
# }

# data2 = {
#     "Date": ["2024-07-06", "2024-07-07", "2024-07-08", "2024-07-09", "2024-07-10"],
#     "Product": ["Tablet", "Mouse", "Monitor", "Keyboard", "Tablet"],
#     "Units_Sold": [8, 15, 10, 12, 6],
#     "Unit_Price": [300, 22, 140, 28, 300],
#     "Total_Sales": [2400, 330, 1400, 336, 1800],
#     "Quality": ["High", "Medium", "Low", "High", "Medium"],
# }

# df = pd.DataFrame(data1)
# df = pd.DataFrame(data2)
# print(df)

# with open("set/fold/sales_data2.csv", 'w') as f:
#     df.to_csv(f, index=False)


# read
# df1 = pd.read_csv("set/fold/sales_data2.csv")
# print(df)
print("==============================")
# df2 = pd.read_csv("set/fold/sales_data1.csv")
# print(df)



# combining data sets #
# combined_data = pd.concat([df1, df2], ignore_index=True)

# df = pd.DataFrame(combined_data)

# df['Region'] = ["East", "North", "West", "North", "South",
#                 "South", "West", "South", "East", "South"] 

# df['Transactions'] = [3, 4, 7, 8, 1, 9, 5, 2, 6, 3]

# df['Quality'] = [10, 20, 40, 60, 20, 80, 40, 10, 90, 70]


# with open("set/fold/h1_sales.csv", 'w') as f:
#     df.to_csv(f, index=False)
#     print("Combined data written to CSV file.")

# print(combined_data)

# df = pd.read_csv("set/fold/h1_sales.csv")
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

# df["Quatity"] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# df.drop(columns=['region'], inplace=True)

# df['Total Amount'] = df['Quatity'] * df['Unit_Price']


# df['HighValue'] = df['Total Amount'] > 1000
# print(df)

# with open("set/fold/h1_sales_updated.csv", 'w') as f:
#     df = pd.DataFrame(df)
#     df.to_csv(f, index=False)
#     print("Updated data written to CSV file.")


#  ================================ TASK 4 ============================= #
# df = pd.read_csv("set/fold/h1_s/
# 

# con = df.groupby('Region').agg({
#     "Total_Sales": "sum",
#     "Quality": "mean",
#     "Transactions": "count"
# })

# con = df.rename(columns={"Total_Sales": "TotalRevenue", "Quality": "AvgQty", "Transactions": "TxnCount"})
# # print(con)
# conn = con.groupby('Region')['TotalRevenue'].count()
# print(conn)


#  =========================== FILTERING ============================= #
# myData = [
#     [ "S001","Guest",3,120,0,"2025-08-01"],
#     ["S002","Member",5,300,0,"2025-08-01"],
#     ["S003","Guest",1,45,1,"2025-08-02"],
#     ["S004","Member",4,200,0,"2025-08-02"],
#     ["S005","Guest",2,80,0,"2025-08-03"],
#     ["S006","Member",6,400,0,"2025-08-03"],
#     ["S007","Guest",1,30,1,"2025-08-03"],
#     ["S008","Member",3,150,0,"2025-08-04"],
#     ["S009","Guest",4,180,0,"2025-08-04"],
#     ["S010","Member",2,90,0,"2025-08-05"],
# ]

# columns = ["SessionID", "UserType", "PageViews", "DurationSec", "Bounce", "Date"]

# df = pd.DataFrame(myData, columns=columns)


# with open("set/fold/web_traffic.csv", 'w') as f:
#     df.to_csv(f, index=False)
    # print("created!")


# with open("set/fold/web_traffic.csv") as f:
    # df = pd.read_csv(f)
    # print(df)
    # con = df[df["UserType"] == 'Member']

    # con = df[(df["UserType"] == 'Member') & (df['PageViews'] >= 4) & (df['Bounce'] == 0)]
    

    # con = df.sort_values(by="DurationSec", ascending=False)
    # print(con.head(10))


# ============================================ DYNAMIC COLUMN HANDLING ========================================== #

# data = [
#     [1,"John Doe","john@example.com","Spring Sale",123,"abc",250,"xyz"],
#     [2,"Jane Smith","jane@example.com","Summer Promo",456,"def",300,789],
#     [3,"Bob Johnson","bob@example.com","Fall Discount",789,"ghi",150,101]
# ]

# columns = ["CustomerID","Name","Email","Campaign","TempData","UnusedMetrics","PurchaseAmount","Unused"]

# df = pd.DataFrame(data, columns=columns)

# with open("set/fold/marketing_campaign.csv", "w") as f:
#     df.to_csv(f, index=False)
#     print("created!")



# df = pd.read_csv("set/fold/marketing_campaign.csv")

# drop_data = [col for col in df.columns if 'TempData' in col or 'Unused' in col]
# # drop_data = [col for col in df.columns if 'TempData' in col or 'Unused' in col]

# newData = df.drop(columns=drop_data)

# df = pd.DataFrame(newData)

# with open("set/fold/marketing_campaign.csv", "w") as f:
#    df.to_csv(f, index=False) 
#    print("done!")



#  ================================= Complex Group‑Filter‑Aggregate Pipeline ================================== #
data = [
    [1,1001,"Electronics","2025-05-15",12000],
    [2,1002,"Clothing","2025-06-20",4000],
    [3,1003,"Home","2025-07-10",15000],
    [4,1002,"Electronics","2025-07-22",8000],
    [5,1004,"Furniture","2025-03-30",7000],
    [6,1005,"Electronics","2025-06-25",30000],
    [7,1001,"Clothing","2025-07-15",6000]
]

# columns = ["OrderID","CustomerID","ProductCategory","OrderDate","SalesAmount"]


# df = pd.DataFrame(data, columns=columns)

# with open("set/fold/orders.csv", "w") as f:
#     df.to_csv(f, index=False)



df = pd.read_csv("set/fold/orders.csv")
print(df)