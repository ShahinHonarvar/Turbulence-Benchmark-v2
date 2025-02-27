def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    existing_numbers = set(numbers[21:93])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_tuple = tuple(range(100))
    result = return_binary_or_hexa(test_tuple)
    print(result)