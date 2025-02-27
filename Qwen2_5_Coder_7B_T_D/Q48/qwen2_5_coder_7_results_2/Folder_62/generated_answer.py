def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers[a:b + 1]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()