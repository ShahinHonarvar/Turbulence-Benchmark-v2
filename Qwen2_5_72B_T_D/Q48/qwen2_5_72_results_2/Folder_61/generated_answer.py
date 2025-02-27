def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[8]
    present = set(numbers[1:8])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check():
    assert return_binary_or_hexa((1, 2, 3, 4, 5, 6, 7, 8, 10)) == '49'
    assert return_binary_or_hexa((5, 6, 7, 8, 9, 10, 11, 12, 15)) == '1e'
    assert return_binary_or_hexa((2, 3, 4, 5, 6, 7, 8, 9, 11)) == 'a'
    assert return_binary_or_hexa((1, 3, 4, 5, 6, 7, 8, 9, 10)) == ''
    print('All tests passed.')