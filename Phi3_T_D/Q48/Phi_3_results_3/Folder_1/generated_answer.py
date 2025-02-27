def return_binary_or_hexa(nums):
    a = nums[17]
    b = nums[88]
    missing_sum = sum(range(a + 1, b)) - sum(set(range(a + 1, b)).difference(set(nums[17:88])))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]