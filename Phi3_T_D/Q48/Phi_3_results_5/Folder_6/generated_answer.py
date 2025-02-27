def return_binary_or_hexa(tuple_nums):
    a = tuple_nums[20]
    b = tuple_nums[93]
    included_nums = set(tuple_nums[20:94])
    excluded_sum = sum((i for i in range(a + 1, b) if i not in included_nums))
    if excluded_sum % 2 == 0:
        return hex(excluded_sum)[2:]
    else:
        return bin(excluded_sum)[2:]