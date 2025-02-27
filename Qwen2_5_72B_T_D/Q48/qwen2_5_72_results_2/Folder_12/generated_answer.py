def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    total_sum = 0
    present_numbers = set(numbers[17:87])
    for i in range(a + 1, b):
        if i not in present_numbers:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_solution():
    test_tuple = tuple((i for i in range(100) if i != 90))
    assert return_binary_or_hexa(test_tuple) == '101100010', 'Test case 1 failed'
    test_tuple = tuple((i for i in range(200)))
    assert return_binary_or_hexa(test_tuple) == '', 'Test case 2 failed'
    test_tuple = tuple((i for i in range(200) if i != 123))
    assert return_binary_or_hexa(test_tuple) == '7b', 'Test case 3 failed'