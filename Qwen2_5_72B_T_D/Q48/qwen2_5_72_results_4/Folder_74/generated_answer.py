def return_binary_or_hexa(data):
    a = data[69]
    b = data[97]
    full_range_set = set(range(a + 1, b))
    data_subset = set(data[70:97])
    missing_numbers = full_range_set - data_subset
    missing_sum = sum(missing_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]