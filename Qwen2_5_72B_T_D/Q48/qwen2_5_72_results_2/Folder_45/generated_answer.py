def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    total_sum = sum(set(range(a + 1, b)) - set(numbers[31:200]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()

def check_function():
    test_numbers = tuple(range(300))
    assert return_binary_or_hexa(test_numbers) == ''
    test_numbers = list(range(300))[:30] + [330] + list(range(301, 307)) + [308, 309, 310] + list(range(312, 300)) + list(range(331, 600))
    assert return_binary_or_hexa(test_numbers) == '11001000001110001000011110001010010100001010011'
    test_numbers = list(range(300))[:30] + [330] + list(range(300, 307)) + list(range(310, 300)) + list(range(331, 600))
    assert return_binary_or_hexa(test_numbers) == '15A4878A0'
    print('All tests passed!')