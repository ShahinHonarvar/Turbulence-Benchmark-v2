def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[3:7]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    assert return_binary_or_hexa((0, 1, 2, 4, 6, 7, 9, 10, 12, 15)) == '3'
    assert return_binary_or_hexa((0, 1, 3, 5, 6, 8, 10, 12, 14, 15)) == '1e'
    assert return_binary_or_hexa((1, 2, 3, 4, 5, 6, 7, 8, 10, 12)) == ''