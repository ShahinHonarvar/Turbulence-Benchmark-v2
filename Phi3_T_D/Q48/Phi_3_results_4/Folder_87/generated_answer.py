def return_binary_or_hexa(nums):
    a, b = (nums[20], nums[43])
    sum_not_present = sum(range(a + 1, b)) - sum(nums[20 + 1:43])
    if sum_not_present % 2 == 0:
        return '{:x}'.format(sum_not_present)
    return '{0:b}'.format(sum_not_present).lstrip('0')