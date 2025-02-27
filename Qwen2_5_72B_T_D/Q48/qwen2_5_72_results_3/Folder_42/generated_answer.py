def return_binary_or_hexa(numbers):
    if len(numbers) < 61 or numbers[18] + 1 >= numbers[60] - 1:
        return ''
    a = numbers[18]
    b = numbers[60]
    full_set = set(range(a + 1, b))
    present_set = set(numbers[19:60])
    missing_numbers_sum = sum(full_set - present_set)
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]

def check_solution():
    test_data = tuple(range(100))
    assert return_binary_or_hexa(test_data) == ''
    test_data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72)
    assert return_binary_or_hexa(test_data) == '1110111000101010011000001100001000001110010110010000000000'
    test_data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72)
    assert return_binary_or_hexa(test_data) == '1e884a10'
    print('All checks passed.')