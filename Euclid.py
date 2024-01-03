# Given two integers a and b where a >= b, compute the remainder r when a is divided by b.
# If r is 0, then the GCD is b.
# If r is not 0, set a = b and b = r, and repeat from step 1.
def euclidenum1n_gcd(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = euclidenum1n_gcd(num1, num2)
print("The GCD is:", result)

#recursion
# def euclidean_recursive_gcd(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return euclidean_recursive_gcd(num2, num1 % num2)
#
# # Example usage:
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result = euclidean_recursive_gcd(num1, num2)
# print("The GCD is:", result)