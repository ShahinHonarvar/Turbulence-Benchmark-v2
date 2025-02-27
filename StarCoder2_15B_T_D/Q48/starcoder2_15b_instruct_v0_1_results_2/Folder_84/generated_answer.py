def return_binary_or_hexa(my_tuple: tuple) -> str:
    a, b = (my_tuple[32], my_tuple[44])
    expected_range = range(a + 1, b)
    actual_range = [num for num in my_tuple[33:44] if num not in expected_range]
    result = sum(actual_range)
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()