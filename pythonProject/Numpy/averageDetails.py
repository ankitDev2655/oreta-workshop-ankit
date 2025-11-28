import numpy as np

data = np.genfromtxt("details.csv", delimiter=",", skip_header=1, usecols=1)

clean_data = data[~np.isnan(data)]

average_amount = np.mean(clean_data)

print("Average Amount:", average_amount)