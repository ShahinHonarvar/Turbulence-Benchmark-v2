def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    full_set = set(range(a + 1, b))
    given_set = set(nums[39:52])
    diff_set = full_set - given_set
    if not diff_set:
        return ''
    total_sum = sum(diff_set)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]