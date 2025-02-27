def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()