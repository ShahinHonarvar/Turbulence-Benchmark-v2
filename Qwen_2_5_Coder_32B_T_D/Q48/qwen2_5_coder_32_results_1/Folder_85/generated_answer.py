def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[8])
    total = 0
    num_set = set(nums[1:9])
    for num in range(a + 1, b):
        if num not in num_set:
            total += num
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].lower()