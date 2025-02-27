def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    sum_of_missing = sum(set(range(a + 1, b)) - set(numbers[57:90]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]

def check_solution():
    test_tuple = tuple(sorted(set(range(100)) - {58, 60, 62}))
    assert return_binary_or_hexa(test_tuple) == '111100', 'Test case 1 failed'
    test_tuple = tuple(range(100))
    assert return_binary_or_hexa(test_tuple) == '', 'Test case 2 failed'
    print('All test cases passed!')