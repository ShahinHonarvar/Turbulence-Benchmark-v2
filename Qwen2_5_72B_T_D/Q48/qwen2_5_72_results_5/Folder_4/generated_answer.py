def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    present_numbers = set(numbers[49:75])
    missing_sum = sum(set(range(a + 1, b)) - present_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]

def check_function():
    example_tuple = tuple(range(100))
    assert return_binary_or_hexa(example_tuple) == '1100011100'
    example_tuple_with_missing = (*range(50), 53, *range(54, 75), 76, *range(77, 100))
    assert return_binary_or_hexa(example_tuple_with_missing) == '110'
    print('All checks passed.')