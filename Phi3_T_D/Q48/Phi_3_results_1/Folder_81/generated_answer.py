def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[100])
    missing_sum = sum(set(range(a + 1, b)).difference(nums[10:100]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return f'{bin(missing_sum)[2:]}'