def return_binary_or_hexa(numbers):
    if len(numbers) < 85:
        return ''
    a = numbers[73]
    b = numbers[84]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[74:84]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_case = tuple(range(100))
    assert return_binary_or_hexa(test_case) == '', 'Case 1 Failed'
    test_case = test_case[:74] + (77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99)
    assert return_binary_or_hexa(test_case) == '111111011110', 'Case 2 Failed'
    test_case = test_case[:74] + (75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 99)
    assert return_binary_or_hexa(test_case) == '3c', 'Case 3 Failed'
    print('All cases passed!')