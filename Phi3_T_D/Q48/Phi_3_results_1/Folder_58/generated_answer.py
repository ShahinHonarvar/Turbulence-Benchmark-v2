def return_binary_or_hexa(nums):
    a, b = (nums[275], nums[871])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in nums[275:871]))
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]