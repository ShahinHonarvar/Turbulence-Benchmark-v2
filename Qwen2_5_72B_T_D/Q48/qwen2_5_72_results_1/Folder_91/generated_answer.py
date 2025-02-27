def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[6]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[1:6]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()