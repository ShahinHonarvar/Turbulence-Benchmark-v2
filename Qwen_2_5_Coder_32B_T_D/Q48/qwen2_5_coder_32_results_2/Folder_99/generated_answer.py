def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    full_set = set(range(a + 1, b))
    given_set = set(nums[428:669])
    diff_set = full_set - given_set
    total_sum = sum(diff_set)
    if total_sum % 2:
        return bin(total_sum)[2:]
    elif total_sum:
        return hex(total_sum)[2:]
    return ''