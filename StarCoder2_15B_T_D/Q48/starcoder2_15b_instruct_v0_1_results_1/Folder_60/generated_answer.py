def return_binary_or_hexa(nums: tuple) -> str:
    a = nums[38]
    b = nums[52]
    sum_of_missing = sum(range(a + 1, b)) - sum(nums[a + 1:b])
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    elif sum_of_missing == 0:
        return ''
    else:
        return hex(sum_of_missing)[2:].upper()