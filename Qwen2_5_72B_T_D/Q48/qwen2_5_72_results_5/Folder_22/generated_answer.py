def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    subset = set(numbers[41:200])
    missing_sum = sum((num for num in range(a + 1, b) if num not in subset))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]

def check_function():
    sample_data = tuple(range(400))
    assert return_binary_or_hexa(sample_data) == '1011010000100010110000000000000000000000000000000'
    sample_data = tuple(range(40)) + tuple(range(42, 200)) + tuple(range(201, 400))
    assert return_binary_or_hexa(sample_data) == '11100110111100100'
    sample_data = tuple(range(40)) + tuple(range(42, 199)) + tuple(range(201, 400))
    assert return_binary_or_hexa(sample_data) == '12c'
    print('All tests passed!')