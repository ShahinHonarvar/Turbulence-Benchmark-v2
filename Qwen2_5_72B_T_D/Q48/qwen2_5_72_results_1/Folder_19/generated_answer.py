def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[2:4]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    assert return_binary_or_hexa((1, 5, 7, 8, 12)) == '32'
    assert return_binary_or_hexa((1, 3, 5, 7, 9)) == '14'
    assert return_binary_or_hexa((1, 2, 3, 4, 5)) == ''
    print('All tests passed')