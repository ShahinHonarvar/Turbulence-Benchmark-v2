def return_binary_or_hexa(nums):
    if len(nums) < 70:
        return ''
    a = nums[34]
    b = nums[69]
    if a + 1 >= b:
        return ''
    missing_sum = 0
    next_index = 35
    for i in range(a + 1, b):
        if next_index < 70 and nums[next_index] == i:
            next_index += 1
        else:
            missing_sum += i
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]