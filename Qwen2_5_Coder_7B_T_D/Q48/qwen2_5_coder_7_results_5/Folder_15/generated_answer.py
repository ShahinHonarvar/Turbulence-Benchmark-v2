def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[4])
    missing_sum = sum(range(a + 1, b)) - sum(nums[1:4])
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()