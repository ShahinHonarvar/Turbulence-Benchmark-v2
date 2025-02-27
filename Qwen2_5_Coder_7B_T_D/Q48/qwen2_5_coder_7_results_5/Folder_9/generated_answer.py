def return_binary_or_hexa(nums):
    a, b = (nums[70], nums[200])
    total_sum = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(nums[70:201])
    if missing_nums:
        total_sum -= sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()