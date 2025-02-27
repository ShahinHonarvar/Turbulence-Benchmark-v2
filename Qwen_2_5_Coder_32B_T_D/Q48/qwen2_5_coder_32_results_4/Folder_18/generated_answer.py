def return_binary_or_hexa(nums):
    a, b = (nums[56], nums[90])
    present = set(nums[57:90])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]