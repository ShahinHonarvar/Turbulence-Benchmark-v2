def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    total_sum = 0
    num_set = set(nums[35:69])
    for num in range(a + 1, b):
        if num not in num_set:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum > 0:
        return hex(total_sum)[2:]
    return ''