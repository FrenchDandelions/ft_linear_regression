from utils import estimatePrice


def load_theta(filename='theta.txt'):
    with open(filename, 'r') as file:
        theta0, theta1 = map(float, file.read().split(','))
    return theta0, theta1


def main():
    theta0, theta1 = load_theta()
    mileage = float(input("Enter the mileage: "))
    estimated_price = estimatePrice(mileage, theta0, theta1)
    print(f"The estimated price for mileage {mileage} is: {estimated_price}")

if __name__ == "__main__":
    main()
