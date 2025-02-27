def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[69:99]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    example_input = tuple(range(1000))
    assert return_binary_or_hexa(example_input) == '0', 'Test case 1 failed'
    example_input_2 = example_input[:69] + (70, 72, 74, 76, 78, 80) + example_input[99:]
    assert return_binary_or_hexa(example_input_2) == '111110110', 'Test case 2 failed'
    example_input_3 = example_input[:69] + (71, 73, 75, 77, 79, 101, 103, 105, 107, 109) + example_input[99:]
    assert return_binary_or_hexa(example_input_3) == '2d2', 'Test case 3 failed'
    print('All test cases passed!')