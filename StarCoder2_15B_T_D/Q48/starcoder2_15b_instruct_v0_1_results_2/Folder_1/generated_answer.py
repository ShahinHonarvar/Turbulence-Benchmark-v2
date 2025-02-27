def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    sum_of_missing = sum(set(range(a + 1, b)) - set(numbers[18:88]))
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()