def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    if a + 1 >= b - 1:
        return ''
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[13:92]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()