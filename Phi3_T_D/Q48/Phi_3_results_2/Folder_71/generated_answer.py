def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    sum_range = sum(set(range(a + 1, b)).difference(set(nums[20:36])))
    if sum_range % 2 == 1:
        return bin(sum_range)[2:]
    elif sum_range % 2 == 0:
        return hex(sum_range)[2:]
    else:
        return ''