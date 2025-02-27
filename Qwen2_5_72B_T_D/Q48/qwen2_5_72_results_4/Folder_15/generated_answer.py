def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    all_nums = set(numbers)
    missing_sum = sum((i for i in range(a + 1, b) if i not in all_nums))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check():
    assert return_binary_or_hexa((1, 2, 3, 4, 6)) == '100'
    assert return_binary_or_hexa((1, 3, 5, 7, 10)) == '1c'
    assert return_binary_or_hexa((1, 2, 3, 4, 5)) == ''
    print('All tests passed.')