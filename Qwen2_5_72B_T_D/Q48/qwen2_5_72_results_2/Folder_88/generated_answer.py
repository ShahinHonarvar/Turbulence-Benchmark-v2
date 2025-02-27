def return_binary_or_hexa(numbers):
    if len(numbers) < 10:
        return ''
    a = numbers[3]
    b = numbers[9]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers:
            missing_sum += num
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_tuple = (1, 2, 3, 4, 6, 8, 9, 10, 13, 15, 17, 18, 20)
    print(return_binary_or_hexa(test_tuple))