import matplotlib.pyplot as plt

# x = [1, 4, 5]  # time
# y = [3, 6, 9]  # distance
# z = [3,6,2]  # distance

# pl.plot(x, color='blue', marker='o', linestyle='solid')
# pl.plot(y, color='blue', marker='o', linestyle='-')
# pl.grid(True)
# pl.title("Time vs Distance")
# pl.xlabel("Time (hours)")
# pl.ylabel("Distance (km)")
# pl.show()





# flavors = ['Vanilla', 'Chocolate', 'Strawberry']
# sales = [30, 45, 20]

# plt.bar(flavors, sales)
# plt.title("Ice Cream Sales")
# plt.xlabel("Flavors")
# plt.ylabel("Sales (in units)")
# plt.show() 




# x = [5,7,8,7,6,9,5,6,7,8]
# y = [99,86,87,88,100,86,103,87,94,78]

# plt.scatter(x, y)
# plt.title("Study Hours vs Test Score")
# plt.show()




# sizes = [20, 30, 25, 25]
# labels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(sizes, labels=labels, autopct='%2.1f%%')
# plt.title("Fruit Basket")
# plt.show()
    


# ======== Sub graphs ========== #
# x = [1, 2, 3, 4]
# y1 = [1, 4, 9, 16]
# y2 = [1, 2, 3, 4]


# plt.subplot(1, 2, 2)   # 1 row, 2 columns, first plot
# plt.plot(x, y1, color="violet")
# plt.grid(True)

# plt.subplot(1, 2, 1)   # second plot
# plt.plot(x, y2, color="orange")
# plt.grid(True)
# plt.show()


#  =============== multiple graphs ============= #
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, color='blue', marker='o', label="Squares")
plt.plot(x, y2, color='red', marker='s', label="Linear")
plt.legend()  # show labels
plt.show()
