def return_binary_or_hexa(nums):
    if not 44 < len(nums) <= 91:
        return ''
    a = nums[44]
    b = nums[91]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[44:92]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]