def return_binary_or_hexa(data):
    a = data[49]
    b = data[74]
    missing_sum = sum(set(range(a + 1, b)) - set(data[50:74]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    example_data = tuple(range(100))
    print(return_binary_or_hexa(example_data))
    example_data_with_gaps = (*range(50), 52, *range(53, 75), 77, *range(78, 100))
    print(return_binary_or_hexa(example_data_with_gaps))