import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,1,4,3,2,6,8,4,1,2]

plt.scatter(x,y, label="stars", color ="purple", 
marker = "*", s= 30)

plt.xlabel("Ground")
plt.ylabel("Position in sky")

plt.legend()

plt.show()