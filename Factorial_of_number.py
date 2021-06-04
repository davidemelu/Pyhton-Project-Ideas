# emelu codes
print("Find the factorial of any number in this program")
num = int(input("Enter Number: "))
if num < 0:
    print("The number must be positive")
else:
    factorial = num * (num - 1)
    print(num,"!","=",factorial)
