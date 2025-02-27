def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[9]
    numbers_in_range = set(range(a + 1, b))
    numbers_present = set(tup[3:10])
    numbers_missing = numbers_in_range - numbers_present
    sum_missing = sum(numbers_missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()