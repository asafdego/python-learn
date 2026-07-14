
number = [10, 12, 3, 45, 74, 67, 34]

bigest = float('-inf')      # float('-inf') is the best generic way to initialize the variable to the smallest  
sec_bigest = float('-inf')  # possible value so that any number in the list will be greater than it.

for num in number:
    if num > bigest:
        sec_bigest = bigest
        bigest = num

    elif bigest > num > sec_bigest :
        sec_bigest = num

print(bigest)
print(sec_bigest)