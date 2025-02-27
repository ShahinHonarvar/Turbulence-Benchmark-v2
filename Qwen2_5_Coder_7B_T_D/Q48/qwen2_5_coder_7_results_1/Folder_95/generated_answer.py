def return_binary_or_hexa(nums):
    a, b = (nums[32], nums[99])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[a:b]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()