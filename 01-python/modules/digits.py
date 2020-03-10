import numpy as np
from sklearn.datasets import load_digits
import math


digits = load_digits()
data = digits.images
y = digits.target
limit = int(data.shape[0]*0.6)
x_train = data[0:limit, :, :]
x_test = data[limit:, :, :]
y_train = y[:limit]
y_test = y[limit:]
memory = {digit: [] for digit in range(0, 10)}

for idx, mat in enumerate(x_train):
    memory[y_train[idx]].append(mat)
for i in range(0, 10):
    memory[i] = np.array(memory[i]).mean(0)

good = 0
for idx, xtest in enumerate(x_test):
    minmse = math.inf
    mindigit = None
    for digit in range(0, 10):
        mse = (np.square(xtest - memory[digit])).mean()
        if mse < minmse:
            minmse = mse
            mindigit = digit
    #print("Real:",y_test[idx]," Estimado:",mindigit)
    if mindigit == y_test[idx]:
        good += 1

print("Avg. precision:", good/(y_test.shape[0]))
