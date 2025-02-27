def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    existing_nums = set(nums[14:91])
    total = 0
    for i in range(a + 1, b):
        if i not in existing_nums:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]