def return_binary_or_hexa(nums):
    a, b = (nums[16], nums[87])
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[16:88]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]