def return_binary_or_hexa(data):
    a = data[3]
    b = data[8]
    missing_sum = sum(set(range(a + 1, b)) - set(data[4:8]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_data = (1, 3, 4, 6, 7, 8, 10, 14, 15, 20)
    assert return_binary_or_hexa(test_data) == '2c'
    test_data = (2, 3, 4, 5, 7, 8, 9, 10, 11, 15)
    assert return_binary_or_hexa(test_data) == ''
    test_data = (0, 1, 2, 3, 5, 7, 8, 9, 12, 20)
    assert return_binary_or_hexa(test_data) == '2a'
    print('All tests passed!')