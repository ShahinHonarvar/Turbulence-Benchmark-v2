def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[200]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[21:200]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]