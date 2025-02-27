def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[451:905]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]