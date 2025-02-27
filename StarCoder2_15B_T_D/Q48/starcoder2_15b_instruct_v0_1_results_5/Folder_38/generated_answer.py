def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    expected_values = set(range(a + 1, b))
    actual_values = set(numbers[37:85])
    missing_values = expected_values - actual_values
    sum_of_missing_values = sum(missing_values)
    if sum_of_missing_values % 2 == 1:
        return bin(sum_of_missing_values)[2:]
    else:
        return hex(sum_of_missing_values)[2:].upper()