def return_binary_or_hexa(nums):
    a = nums[81]
    b = nums[86]
    existing_numbers = set(nums[81:87])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()