def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    present_numbers = set(numbers[201:202])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]

def check_function():
    test_tuple = tuple(range(300)) + (301,) * 10 + tuple(range(312, 400))
    assert return_binary_or_hexa(test_tuple) == '302'
    test_tuple2 = tuple(range(400))
    assert return_binary_or_hexa(test_tuple2) == ''
    print('All tests passed.')