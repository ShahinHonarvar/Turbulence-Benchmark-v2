def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    total_sum = 0
    missing_nums = set(range(a + 1, b)) - set(nums[13:71])
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]