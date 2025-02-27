def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[77:85]]
    total = sum(missing_nums)
    return bin(total)[2:] if total % 2 else '{:x}'.format(total)