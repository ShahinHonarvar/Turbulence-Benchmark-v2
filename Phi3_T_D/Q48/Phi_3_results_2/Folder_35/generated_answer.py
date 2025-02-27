def return_binary_or_hexa(nums):
    a, b = (nums[77], nums[84])
    missing_nums_sum = sum(range(a + 1, b), start=0) - sum(nums[77:84 + 1])
    if missing_nums_sum < 0:
        return ''
    return bin(missing_nums_sum)[2:] if missing_nums_sum % 2 else hex(missing_nums_sum)[2:]