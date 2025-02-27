def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[45:91]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_tuple = tuple(range(100))
    print(return_binary_or_hexa(test_tuple))
    test_tuple_with_missing = test_tuple[:45] + (47, 49, 51, 53) + test_tuple[91:]
    print(return_binary_or_hexa(test_tuple_with_missing))