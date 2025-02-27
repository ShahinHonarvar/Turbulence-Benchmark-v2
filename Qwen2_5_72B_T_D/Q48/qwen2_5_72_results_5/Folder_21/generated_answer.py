def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    existing_numbers = set(numbers[16:57])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    sample_input = tuple(range(100))
    assert return_binary_or_hexa(sample_input) == ''
    sample_input_2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20) + tuple(range(22, 100))
    assert return_binary_or_hexa(sample_input_2) == '16'
    print('All checks passed.')