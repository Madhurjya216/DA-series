
import matplotlib.pyplot as plt
import pandas as pd
import json

# x = [1, 2, 3, 4, 5] 
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, color='green', marker='^', linestyle='dashed')
# plt.title("Practice Styling")
# plt.grid(True)
# plt.show()



# ================== csv data =================== #
# df = pd.read_csv('D:\Workspace\PYTHON\Data Analytics\mathplotlib\orders.csv')

# plt.plot(df['OrderDate'], df['SalesAmount'], label='Sales Amount')
# plt.xlabel("Order Date")
# plt.ylabel("Sales Amount")
# plt.title("Sales Amount by Order Date")
# plt.grid(True)
# plt.legend()
# plt.show()



# =================== json data =================== #
# df = pd.read_json('D:\Workspace\PYTHON\Data Analytics\mathplotlib\data.json')
# # data = pd.read_json(df)
# # name = data['name']
# # age = data['age']
# # city = data['city']

# plt.plot(df['name'], df['age'], linestyle='solid', marker='o', color='red')
# plt.grid(True)
# plt.show()

# print(df)


# trail data set - MATPLOTLIB

# SET 1:
# x = [1,2,3,4,5] 
# y = [2,4,6,8,10]

# plt.plot(x, y, color='red', marker='o', linestyle='dashed')
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Simple Plot")
# plt.grid(True)
# plt.show()


# SET 2:
# fruits = ["Apple", "Banana", "Cherry", "Date"]
# sales = [40, 25, 30, 10]


# plt.bar(fruits, sales, color=['red', 'yellow', 'pink', 'brown'])
# plt.show()


# SET 3:
# fruits = ["Apple", "Banana", "Cherry", "Date"]
# sales = [40, 25, 30, 10]

# plt.pie(sales, labels=fruits, autopct='%1.1f%%')
# plt.legend()
# plt.show()

import numpy as np
x = np.random.randint(1, 50, 20)
y = np.random.randint(1, 50, 20)

plt.plot(x, y, marker='x')
plt.show()