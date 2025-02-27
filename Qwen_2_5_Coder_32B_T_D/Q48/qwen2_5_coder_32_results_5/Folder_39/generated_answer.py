def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[91])
    total_sum = 0
    used = set(nums[45:91])
    for i in range(a + 1, b):
        if i not in used:
            total_sum += i
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]