import matplotlib.pyplot as plt
import random

# Generate random data for two lists
num_points = 50
list1 = [random.randint(1, 100) for _ in range(num_points)]
list2 = [random.randint(1, 100) for _ in range(num_points)]

# Create a scatter plot
plt.scatter(list1, list2, color='blue', marker='o')

# Label the axes
plt.xlabel('List 1')
plt.ylabel('List 2')
plt.title('Scatter Plot of Two Random Lists')

# Show the plot
plt.show()

