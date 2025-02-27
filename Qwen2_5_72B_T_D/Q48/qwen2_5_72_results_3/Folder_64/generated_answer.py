def return_binary_or_hexa(nums):
    a, _, _, _, _, b = nums
    missing_sum = sum(set(range(a + 1, b)) - set(nums))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    assert return_binary_or_hexa((1, 3, 5, 7, 9, 11)) == '24'
    assert return_binary_or_hexa((2, 4, 6, 8, 10, 12)) == '1c'
    assert return_binary_or_hexa((0, 1, 2, 3, 4, 5)) == ''
    print('All tests passed.')