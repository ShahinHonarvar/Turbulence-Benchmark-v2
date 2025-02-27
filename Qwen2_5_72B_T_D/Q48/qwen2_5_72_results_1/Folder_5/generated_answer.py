def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[3:8]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    assert return_binary_or_hexa((1, 3, 5, 7, 9, 11, 13, 15, 19, 21)) == '100110'
    assert return_binary_or_hexa((2, 4, 6, 7, 8, 9, 10, 11, 13, 15)) == '6'
    assert return_binary_or_hexa((5, 10, 12, 13, 14, 15, 16, 17, 18, 20)) == '11'
    assert return_binary_or_hexa((10, 20, 30, 32, 34, 36, 38, 40, 42, 50)) == ''
    print('All checks pass.')