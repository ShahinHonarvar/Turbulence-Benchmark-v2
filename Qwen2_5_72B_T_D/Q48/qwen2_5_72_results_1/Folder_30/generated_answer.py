def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[23:24]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]