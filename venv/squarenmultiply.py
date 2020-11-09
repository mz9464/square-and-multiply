"""
file: squarenmutliply.py
author: Misty Zheng
description: Prints out the steps in the square-and-mulitply algorithm
            Used in RSA encryption for fast exponentiation
"""

def square_n_muliply(base, exp, mod):
    exp = bin(exp)
    value = base
    print("h0\n" + str(base))
    for i in range(3, len(exp)):
        print("\nh" + str(i-2))
        print(str(value%mod) + "^2" + " = "  + str(value*value%mod))
        value = value * value
        if (exp[i:i + 1] == '1'):
            print(str(value%mod) + "*" + str(base) + " mod " + str(mod) + " = " +  str(value*base%mod))
            value = value * base
    return str(value%mod)

def main():
    base = int(input("Enter base value: "))
    exp = int(input("Enter exponent value: "))
    mod = int(input("Enter modulus value: "))
    print("\n" + str(square_n_muliply(base, exp, mod)))

if __name__ == '__main__':
    main()
