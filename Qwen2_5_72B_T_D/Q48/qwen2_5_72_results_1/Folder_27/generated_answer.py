def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[87:89]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    example_tuple = tuple((i for i in range(1000)))
    print(return_binary_or_hexa(example_tuple))
    example_tuple = (*range(1000),)[:-4] + (996, 1002)
    print(return_binary_or_hexa(example_tuple))