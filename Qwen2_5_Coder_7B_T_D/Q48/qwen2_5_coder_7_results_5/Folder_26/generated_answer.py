def return_binary_or_hexa(nums):
    a, b = (nums[68], nums[99])
    if a + 1 >= b - 1:
        return ''
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[a + 1:b - 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]