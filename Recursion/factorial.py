#!/home/mhyde/vEnvs/py36/bin/python

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


input = int(input("Enter A Number:  "))
print(factorial(input))

string = str(factorial(input))
print(len(string))