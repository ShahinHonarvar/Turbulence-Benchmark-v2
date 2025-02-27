def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[10])
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[1:10]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    example1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15)
    example2 = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16)
    assert return_binary_or_hexa(example1) == '64' or return_binary_or_hexa(example1) == '40', 'Example 1 failed'
    assert return_binary_or_hexa(example2) == '1e' or return_binary_or_hexa(example2) == '30', 'Example 2 failed'
    print('All examples passed')