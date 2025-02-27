def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[1:4]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    assert return_binary_or_hexa((1, 2, 3, 4, 6)) == '5'
    assert return_binary_or_hexa((1, 2, 3, 5, 7)) == '4'
    assert return_binary_or_hexa((1, 3, 5, 7, 9)) == '2c'
    assert return_binary_or_hexa((1, 2, 3, 4, 5)) == ''
    print('All tests passed.')