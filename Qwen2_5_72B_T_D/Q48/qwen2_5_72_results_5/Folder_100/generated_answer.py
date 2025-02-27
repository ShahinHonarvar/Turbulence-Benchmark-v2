def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    present_numbers = set(numbers[45:78])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_solution():
    test_data = tuple(range(100))
    result = return_binary_or_hexa(test_data)
    print(result)
    test_data = tuple(list(range(100))[:45] + list(range(101, 104)) + list(range(104, 100)))
    result = return_binary_or_hexa(test_data)
    print(result)