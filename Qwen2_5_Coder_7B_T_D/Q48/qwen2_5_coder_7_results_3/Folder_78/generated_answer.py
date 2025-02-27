def return_binary_or_hexa(nums):
    a, b = (nums[62], nums[96])
    total_sum = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(nums[62:97])
    for num in missing_nums:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]