def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[4]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[1:4]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    assert return_binary_or_hexa((1, 2, 3, 4, 10)) == '1010', 'Test case 1 failed'
    assert return_binary_or_hexa((0, 1, 2, 4, 8)) == '7', 'Test case 2 failed'
    assert return_binary_or_hexa((10, 11, 12, 13, 14)) == '', 'Test case 3 failed'
    print('All test cases passed!')