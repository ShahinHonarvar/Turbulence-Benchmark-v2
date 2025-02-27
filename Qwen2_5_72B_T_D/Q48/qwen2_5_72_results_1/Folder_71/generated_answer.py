def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    present_nums = set(nums[21:35])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_nums))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]