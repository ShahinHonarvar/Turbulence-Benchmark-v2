def return_binary_or_hexa(nums):
    a = nums[17]
    b = nums[88]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[18:88]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]