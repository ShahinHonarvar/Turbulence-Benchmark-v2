def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[88]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[56:89]))
    if missing_sum == 0:
        return ''
    else:
        return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]