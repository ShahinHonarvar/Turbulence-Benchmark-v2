def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(nums[10:98])
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()