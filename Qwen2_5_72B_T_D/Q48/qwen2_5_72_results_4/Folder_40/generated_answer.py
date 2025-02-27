def return_binary_or_hexa(nums):
    a, _, _, b = nums
    full_set = set(range(a + 1, b))
    tuple_set = set(nums[1:3])
    difference_set = full_set - tuple_set
    total_sum = sum(difference_set)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]