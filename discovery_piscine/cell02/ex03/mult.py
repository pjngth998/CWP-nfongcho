print("Enter the first number:")
x = int(input())
print("Enter the second number:")
y = int(input())
mul = x*y
print(f"{x} x {y} = {mul}")
if mul == 0:
    print("the result is positive and negative.")
elif mul > 0:
    print("the result is positive.")
else:
    print("the result is negative.")