def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    complete_set = set(range(a + 1, b))
    in_tuple_set = set(nums[29 + 1:53 + 1])
    missing_nums = complete_set - in_tuple_set
    total_sum = sum(missing_nums)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]