from utils import load_data, formula
import numpy as np
import matplotlib.pyplot as plt

def save_theta(theta0, theta1, filename='theta.txt'):
    with open(filename, 'w') as file:
        file.write(f"{theta0},{theta1}")


def get_coeff(mileage, price):
    n = np.size(mileage)

    m_x = np.mean(mileage)
    m_y = np.mean(price)

    ss_xy = np.sum(price * mileage) - n * m_y * m_x
    ss_xx = np.sum(mileage * mileage) - n * m_x * m_x
    theta_1 = ss_xy / ss_xx
    theta_0 = m_y - theta_1 * m_x
    return(theta_0, theta_1)

def main():
    mileage, price = load_data('data.csv')
    print(mileage, price)
    t0, t1 = formula(0.0001, mileage, price)
    save_theta(t0, t1)


if __name__ == "__main__":
    main()
