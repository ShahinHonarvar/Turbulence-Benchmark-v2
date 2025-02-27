def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[450:906]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()