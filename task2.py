
number = [10, 12, 3, 45, 74, 67, 34]

bigest = number[0]
sec_bigest = number[0]

for num in number:
    if num > bigest:
        sec_bigest = bigest
        bigest = num
        
    elif bigest > num > sec_bigest :
        sec_bigest = num

print(bigest)
print(sec_bigest)