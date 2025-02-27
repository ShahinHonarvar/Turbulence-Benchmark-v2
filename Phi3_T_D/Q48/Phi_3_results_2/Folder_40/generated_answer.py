def return_binary_or_hexa(numbers):
    a, _, _, b = numbers
    sum_of_missing = sum(set(range(a + 1, b)).difference(numbers))
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]