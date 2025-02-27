def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[2:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]