def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[36]
    present = set(numbers[20:37])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    example1 = tuple(range(100))
    example2 = (1, 2, 3, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 50, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 75)
    assert return_binary_or_hexa(example1) == ''
    assert return_binary_or_hexa(example2) in ['1111111111111', '1fff']
    print('All checks pass.')