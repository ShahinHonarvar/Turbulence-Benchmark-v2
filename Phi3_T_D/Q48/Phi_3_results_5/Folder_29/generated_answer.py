def return_binary_or_hexa(nums):
    a, b = (nums[70], nums[98])
    sum_not_present = sum(set(range(a + 1, b)) - set(nums[70:99]))
    if sum_not_present % 2 != 0:
        return f'{bin(sum_not_present)[2:]}'
    else:
        return f'{hex(sum_not_present)[2:].upper()}'