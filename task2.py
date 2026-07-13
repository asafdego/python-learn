
number = [10, 74, 3, 45, 12, 67, 34]

smallest = number[0]

for num in number:
    if num < smallest:
        smallest = num

print(smallest)