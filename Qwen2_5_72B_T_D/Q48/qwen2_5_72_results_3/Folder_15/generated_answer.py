def return_binary_or_hexa(nums):
    a, _, _, _, b = nums
    missing_sum = sum(set(range(a + 1, b)) - set(nums))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    assert return_binary_or_hexa((1, 2, 3, 4, 6)) == '5'
    assert return_binary_or_hexa((0, 1, 3, 6, 9)) == 'f'
    assert return_binary_or_hexa((5, 6, 7, 8, 9)) == ''