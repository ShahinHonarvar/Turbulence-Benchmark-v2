def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    numbers_in_range = set(range(a + 1, b))
    numbers_in_tuple = set(t[34:78])
    sum_of_numbers = sum(numbers_in_range - numbers_in_tuple)
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].upper()