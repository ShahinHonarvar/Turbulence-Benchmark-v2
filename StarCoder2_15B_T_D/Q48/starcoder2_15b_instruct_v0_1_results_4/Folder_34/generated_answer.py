def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[200]
    missing_numbers = set(range(a + 1, b)) - set(tup[a + 1:b])
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]