def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[36:54 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]