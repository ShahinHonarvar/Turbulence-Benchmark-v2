def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[51:200]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_case = tuple(range(300))
    assert return_binary_or_hexa(test_case) == '100101000000000', 'Test case 1 failed'
    test_case = tuple([i for i in range(300) if i != 150])
    assert return_binary_or_hexa(test_case) == '90', 'Test case 2 failed'
    test_case = tuple([0] * 300)
    assert return_binary_or_hexa(test_case) == '', 'Test case 3 failed'