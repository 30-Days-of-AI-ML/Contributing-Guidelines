# python code to change temperature
# from celcius to farenhite & viceversa
# input your temp and change it

# Define a function to convert
# celsius temperature to Fahrenheit


def Celsius_to_Fahrenheit(c):
    f = (9/5)*c + 32
    return f

# Define a function to convert
# Fahrenheit temperature to Celsius


def Fahrenheit_to_Celsius(f):
    c = (5/9)*(f - 32)
    return c


# Driver Code
if __name__ == "__main__":
    c = float(input('Enter temperature in Celsius: '))
    print(c, "celsius is equal to:", Celsius_to_Fahrenheit(c), "Fahrenheit")
    f = float(input('Enter temperature in Fahrenheit: '))
    print(f, "Fahrenheit is equal to:", Fahrenheit_to_Celsius(f), "celsius")
