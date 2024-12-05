import numpy as np
import pandas as pd

epochs=100

def load_data(filename):
    mileage = []
    price = []
    tab = pd.read_csv(filename)
    mileage, price = tab.iloc[:, 0], tab.iloc[:, 1]
    print(mileage, price, sep="\n")
    return np.array(mileage), np.array(price)

def estimatePrice(mileage, t0, t1):
    return t0 + (t1 * mileage)

def formula(learningRate, mileage, price):
    theta0, theta1 = 0, 0
    for _ in range(epochs):
        t0, t1 = 0, 0
        for i in range(len(mileage)):
            error  = estimatePrice(mileage[i], theta0, theta1) - price[i]
            t0 += error
            t1 += error * mileage[i]
        t0 = (learningRate / len(mileage)) * t0
        t1 = (learningRate / len(mileage)) * t1
        theta0 -= t0
        theta1 -= t1

    return theta0, theta1

