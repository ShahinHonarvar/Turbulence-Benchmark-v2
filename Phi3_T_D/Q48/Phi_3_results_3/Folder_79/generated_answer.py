def return_binary_or_hexa(nums):
    if len(nums) < 8:
        return ''
    a, b = (nums[1], nums[7])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[1:8]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]