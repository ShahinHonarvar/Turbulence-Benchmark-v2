def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[7]
    missing_sum = sum(range(a + 1, b)) - sum(nums[1:8]) - a - b
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]