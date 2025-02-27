def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[78]
    sum_missing = 0
    num_set = set(nums[44:79])
    for num in range(a + 1, b):
        if num not in num_set:
            sum_missing += num
    if sum_missing == 0:
        return ''
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]