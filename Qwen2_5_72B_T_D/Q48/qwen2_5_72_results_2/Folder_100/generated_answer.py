def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[45:78]:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    data = tuple(range(100))
    assert return_binary_or_hexa(data) == '', 'Test case 1 failed'
    data = data[:45] + (100, 101, 102) + data[79:]
    assert return_binary_or_hexa(data) == '3ff', 'Test case 2 failed'
    data = data[:45] + (45, 78) + data[79:]
    assert return_binary_or_hexa(data) == '4d2', 'Test case 3 failed'
    print('All test cases passed!')