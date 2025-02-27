def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[8]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[2:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test1 = (0, 1, 2, 3, 4, 5, 6, 7, 10)
    test2 = (0, 1, 3, 4, 5, 6, 7, 8, 10)
    test3 = (0, 1, 2, 3, 4, 5, 6, 7, 11)
    print(return_binary_or_hexa(test1))
    print(return_binary_or_hexa(test2))
    print(return_binary_or_hexa(test3))