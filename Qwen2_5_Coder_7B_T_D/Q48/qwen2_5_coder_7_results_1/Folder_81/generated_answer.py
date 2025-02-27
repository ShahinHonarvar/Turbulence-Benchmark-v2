def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    total_sum = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(nums[a + 1:b])
    total_sum -= sum(missing_nums)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]