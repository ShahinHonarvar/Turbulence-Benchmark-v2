def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[8]
    num_set = set(tup[4:8])
    missing_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    assert return_binary_or_hexa((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == ''
    assert return_binary_or_hexa((0, 1, 2, 4, 5, 6, 8, 9, 10, 12)) == '2b'
    assert return_binary_or_hexa((0, 1, 2, 4, 5, 6, 7, 9, 11, 15)) == '1010'
    print('All checks passed.')