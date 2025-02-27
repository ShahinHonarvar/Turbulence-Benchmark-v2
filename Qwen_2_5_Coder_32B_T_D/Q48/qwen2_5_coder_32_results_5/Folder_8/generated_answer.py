def return_binary_or_hexa(nums):
    a, b = (nums[45], nums[48])
    total_sum = 0
    num_set = set(nums[46:48])
    for num in range(a + 1, b):
        if num not in num_set:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]