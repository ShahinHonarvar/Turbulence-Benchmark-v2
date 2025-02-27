def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[3:7]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check():
    assert return_binary_or_hexa((0, 2, 4, 6, 8, 10, 12, 14, 16)) == '100'
    assert return_binary_or_hexa((1, 2, 3, 4, 5, 6, 7, 8, 9)) == ''
    assert return_binary_or_hexa((0, 1, 3, 4, 6, 8, 10, 11, 13)) == '4d'