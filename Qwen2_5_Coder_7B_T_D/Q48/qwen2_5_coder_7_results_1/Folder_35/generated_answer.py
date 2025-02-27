def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    total_sum = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(nums[78:84])
    actual_sum = sum(missing_nums)
    if actual_sum % 2 == 1:
        return bin(actual_sum)[2:]
    else:
        return hex(actual_sum)[2:].upper()