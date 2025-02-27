def return_binary_or_hexa(nums):
    a, b = (nums[32], nums[44])
    total = 0
    num_set = set(nums[33:44])
    for num in range(a + 1, b):
        if num not in num_set:
            total += num
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]