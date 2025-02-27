def return_binary_or_hexa(nums):
    if len(nums) < 30 or 200 >= len(nums):
        return ''
    a, b = (nums[29], nums[199])
    missing_sum = sum((n for n in range(a + 1, b) if n not in nums[30:200]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]