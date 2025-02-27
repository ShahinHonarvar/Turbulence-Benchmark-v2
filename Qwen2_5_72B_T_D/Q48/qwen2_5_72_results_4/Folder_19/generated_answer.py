def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[2:4]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    assert return_binary_or_hexa((1, 3, 5, 8, 10)) == '1001'
    assert return_binary_or_hexa((1, 2, 3, 4, 5)) == ''
    assert return_binary_or_hexa((0, 5, 8, 12, 18)) == '17'