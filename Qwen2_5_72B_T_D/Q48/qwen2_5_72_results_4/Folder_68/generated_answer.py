def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check():
    assert return_binary_or_hexa((1, 2, 3, 4, 5, 6, 7, 8, 9, 15)) == '63'
    assert return_binary_or_hexa((10, 11, 12, 13, 14, 15, 16, 17, 18, 25)) == '57'
    assert return_binary_or_hexa((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) == ''