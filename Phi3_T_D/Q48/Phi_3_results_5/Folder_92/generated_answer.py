def return_binary_or_hexa(nums):
    a, _, b = (nums[0], nums[1], nums[2])
    missing_sum = sum(set(range(a + 1, b)).difference(nums[0:3]))
    result = ''
    if missing_sum % 2 != 0:
        result = bin(missing_sum)[2:]
    else:
        result = hex(missing_sum)[2:]
    return result