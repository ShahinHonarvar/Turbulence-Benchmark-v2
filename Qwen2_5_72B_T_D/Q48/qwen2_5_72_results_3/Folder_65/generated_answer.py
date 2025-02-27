def return_binary_or_hexa(nums):
    a = nums[51]
    b = nums[76]
    present = set(nums[51:77])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]