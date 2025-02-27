def return_binary_or_hexa(nums):
    a, b = (nums[35], nums[64])
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[35:65]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]