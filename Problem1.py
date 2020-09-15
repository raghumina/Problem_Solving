# Python Problem Solving
# Link of Problem: https://www.hackerrank.com/challenges/solve-me-first/problem
# Problwm name: Solve me first

# lets Start:
# Complete the function solveMeFirst to compute the sum of two integers.
#
# Function prototype:
#
# int solveMeFirst(int a, int b);
#
# where,
#
# a is the first integer input.
# b is the second integer input
# Return values
#
# sum of the above two integers
# Sample Input
#
# a = 2
# b = 3
# Sample Output
#
# 5
# Explanation
#
# The sum of the two integers  and  is computed as: .


# given code
'''

def solveMeFirst(a,b):
	# Hint: Type return a+b below


    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2
    return sum
print(sum)


'''
# my answer
def solveMeFirst(a, b):
    sum = a + b
    return sum


a = int(input())
b = int(input())
print(solveMeFirst(a, b))
