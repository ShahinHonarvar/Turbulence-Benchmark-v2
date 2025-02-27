def return_binary_or_hexa(nums):
    a, b = (nums[3], nums[9])
    total_sum = 0
    num_set = set(nums[3:10])
    for i in range(a + 1, b):
        if i not in num_set:
            total_sum += i
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]