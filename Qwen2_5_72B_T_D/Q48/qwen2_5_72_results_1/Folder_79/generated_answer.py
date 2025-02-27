def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[2:7]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test1 = return_binary_or_hexa((1, 3, 4, 6, 7, 8, 9, 12))
    assert test1 == '3c', f'Test 1 failed, got {test1}'
    test2 = return_binary_or_hexa((0, 2, 3, 4, 5, 6, 7, 9))
    assert test2 == '', f'Test 2 failed, got {test2}'
    test3 = return_binary_or_hexa((2, 4, 6, 8, 10, 12, 14, 16))
    assert test3 == '1110', f'Test 3 failed, got {test3}'
    print('All tests passed!')