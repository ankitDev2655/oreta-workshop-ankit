# import numpy as np

# # Load the CSV file (skip header, second column is amount)
# data = np.genfromtxt('Orders.csv', delimiter=',', skip_header=1, usecols=1)

# # Calculate the average
# average_amount = np.mean(data)

# print("Average Amount:", average_amount)



# import numpy as np

# data = np.genfromtxt("orders.csv", delimiter=",", skip_header=1, usecols=5)
# average_amount = np.mean(data)

# print("Average Amount:", average_amount)




import numpy as np

# Load entire CSV as strings (prevents column errors)
data = np.genfromtxt(
    "orders.csv",
    delimiter=",",
    dtype=str,
    skip_header=1
)

# Extract columns
order_ids = data[:, 0]
order_dates = data[:, 1]
customer_names = data[:, 2]
states = data[:, 3]
cities = data[:, 4]

# Print basic information
print("Total Orders:", len(order_ids))
print("Unique States:", len(np.unique(states)))
print("Unique Cities:", len(np.unique(cities)))

# Count orders per state
unique_states, state_counts = np.unique(states, return_counts=True)

print("\nOrders Per State:")
for state, count in zip(unique_states, state_counts):
    print(f"{state}: {count}")

# Count orders per city
unique_cities, city_counts = np.unique(cities, return_counts=True)

print("\nOrders Per City:")
for city, count in zip(unique_cities, city_counts):
    print(f"{city}: {count}")


# Average Order 
