def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[10])
    full_set = set(range(a + 1, b))
    subset_set = set(numbers[1:11])
    missing_set = full_set - subset_set
    missing_sum = sum(missing_set)
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]