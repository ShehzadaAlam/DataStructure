reversed = 0
remainder = 0
number = 3456

while number > 0:
    remainder = number % 10
    number = number // 10
    reversed = reversed * 10 + remainder
print(reversed)
