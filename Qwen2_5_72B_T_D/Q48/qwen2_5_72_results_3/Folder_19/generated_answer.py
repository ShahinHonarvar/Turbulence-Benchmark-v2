def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    sum_missing = 0
    for num in range(a + 1, b):
        if num not in nums:
            sum_missing += num
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing == 0:
        return ''
    else:
        return hex(sum_missing)[2:]

def check_function():
    assert return_binary_or_hexa((0, 1, 3, 4, 6, 8, 10, 12)) == '4'
    assert return_binary_or_hexa((0, 1, 2, 3, 4, 6, 8, 10, 12)) == '5'
    assert return_binary_or_hexa((0, 1, 2, 3, 4, 5, 6, 10, 12)) == ''