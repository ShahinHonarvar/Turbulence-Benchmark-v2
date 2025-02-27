def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[28])
    total = sum(range(a + 1, b))
    missing = [x for x in range(a + 1, b) if x not in nums[10:29]]
    total -= sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]