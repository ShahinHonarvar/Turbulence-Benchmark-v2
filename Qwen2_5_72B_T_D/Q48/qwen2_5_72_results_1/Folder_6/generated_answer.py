def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[21:93]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]