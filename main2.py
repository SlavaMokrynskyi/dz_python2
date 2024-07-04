import random

str1 = str(input("Enter arithmetic expression(like 23+12) --> "))
parts = []
nums = ""
for i in str1:
    if i.isdigit():
        nums += i
    else:
        parts.append(int(nums))
        parts.append(i)
        nums = ""
parts.append(int(nums))
if parts[1] == '+':
    result = parts[0] + parts[2]
elif parts[1] == '-':
    result = parts[0] - parts[2]
elif parts[1] == '*':
    result = parts[0] * parts[2]
elif parts[1] == '/':
    result = parts[0] / parts[2]
print(f"Result: {result}")

list = []
num = 0
count_minus = 0
count_zeros = 0
count_plus = 0
max_num = 0
min_num = 0
count = int(input("Enter how much numbers generate in list --> "))
diapazon_1 = int(input("Enter first diapazon for random nums --> "))
diapazon_2 = int(input("Enter second diapazon for random nums --> "))
for i in range(count):
    num = random.randint(diapazon_1, diapazon_2)
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
    list.append(num)
    if num < 0:
        count_minus += 1
    elif num == 0:
        count_zeros += 1
    else:
        count_plus += 1
else:
    print(f"Max num is {max_num}")
    print(f"Min num is {min_num}")
    print(f"Count of num < 0 is {count_minus}\nCount of zeros is {count_zeros}\nCount of nums > 0 is {count_plus}")
