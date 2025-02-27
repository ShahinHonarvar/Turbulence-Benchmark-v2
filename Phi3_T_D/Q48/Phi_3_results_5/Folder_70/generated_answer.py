def return_binary_or_hexa(nums):
    a = nums[43]
    b = nums[70]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[43:71]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]