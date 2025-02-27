def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    exclusive_sum = sum((i for i in range(a + 1, b) if i not in nums[34:69]))
    if exclusive_sum % 2 == 1:
        return bin(exclusive_sum)[2:]
    else:
        return format(exclusive_sum, 'x')