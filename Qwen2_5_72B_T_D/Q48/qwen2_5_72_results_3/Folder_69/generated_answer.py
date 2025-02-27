def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[40:43]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]

def check_function():
    test_tuple = tuple(range(100))
    assert return_binary_or_hexa(test_tuple) == '11011110'
    test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 50, 52, 53, 54, 55)
    assert return_binary_or_hexa(test_tuple) == '1c'
    print('All tests passed.')