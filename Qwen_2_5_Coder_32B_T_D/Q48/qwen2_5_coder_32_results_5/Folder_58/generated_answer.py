def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]
    nums_set = set(nums[276:871])
    total_sum = sum((x for x in range(a + 1, b) if x not in nums_set))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]