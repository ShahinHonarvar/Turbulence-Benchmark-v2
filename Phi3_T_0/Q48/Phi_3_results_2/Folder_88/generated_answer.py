def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[3:10]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]