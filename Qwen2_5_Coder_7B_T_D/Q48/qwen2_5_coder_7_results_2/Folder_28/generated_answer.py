def return_binary_or_hexa(nums):
    a, b = (nums[86], nums[99])
    total = sum((x for x in range(a + 1, b) if x not in nums))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()