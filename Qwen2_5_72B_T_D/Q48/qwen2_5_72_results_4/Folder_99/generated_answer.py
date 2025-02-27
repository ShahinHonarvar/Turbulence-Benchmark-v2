def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[428:669]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_tuple = tuple(range(1000))
    assert return_binary_or_hexa(test_tuple) == ''
    test_tuple = test_tuple[:427] + (0,) + test_tuple[428:669] + (1234,) + test_tuple[670:]
    assert return_binary_or_hexa(test_tuple) == '1111010010'
    test_tuple = test_tuple[:427] + (0, 2) + test_tuple[429:669] + (1234,) + test_tuple[670:]
    assert return_binary_or_hexa(test_tuple) == '1'
    test_tuple = test_tuple[:427] + (0,) + test_tuple[428:669] + (1234,) + test_tuple[670:]
    assert return_binary_or_hexa(test_tuple) == '1111010010'