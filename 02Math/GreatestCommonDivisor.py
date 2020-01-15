Given 2 non negative integers m and n, find gcd(m, n)

# GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
# Both m and n fit in a 32 bit signed integer.

# Example

# m : 6
# n : 9


def gcd(a,b):
    while(b):
        a, b = b, a % b

    return a

if __name__=="__main__":
    num1 = int(input("Type first number a: "))
    num2 = int(input("Type second number b: "))
    res=gcd(num1,num2)
    print("the common devisor of {} and {} wil be {}".format(num1,num2,res))
