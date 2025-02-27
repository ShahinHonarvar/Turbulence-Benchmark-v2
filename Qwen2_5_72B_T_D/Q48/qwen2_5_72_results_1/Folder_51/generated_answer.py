def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[7:9]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check():
    assert return_binary_or_hexa((1, 2, 3, 4, 5, 6, 10, 12, 14, 15, 16)) == '110'
    assert return_binary_or_hexa((1, 3, 5, 7, 9, 11, 20, 22, 23, 25, 27, 29, 31)) == '15'
    assert return_binary_or_hexa((0, 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15)) == ''
    assert return_binary_or_hexa((0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)) == '11010'