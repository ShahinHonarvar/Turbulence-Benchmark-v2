def return_binary_or_hexa(data):
    a = data[20]
    b = data[36]
    missing_sum = sum(set(range(a + 1, b)) - set(data[21:36]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    data = tuple(range(100))
    assert return_binary_or_hexa(data) == 'b1011100110101110001100000000000'
    data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32, 34, 36)
    assert return_binary_or_hexa(data) == 'e1'
    data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)
    assert return_binary_or_hexa(data) == ''
    print('All checks passed.')