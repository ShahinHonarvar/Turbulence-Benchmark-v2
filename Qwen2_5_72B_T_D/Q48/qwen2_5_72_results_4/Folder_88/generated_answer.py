def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[9]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[4:9]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()

def check_function():
    test_tup = (0, 1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14)
    print(return_binary_or_hexa(test_tup))