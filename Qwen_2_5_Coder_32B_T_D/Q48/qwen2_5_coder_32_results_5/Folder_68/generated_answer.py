def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[9])
    total_sum = 0
    num_set = set(nums)
    for i in range(a + 1, b):
        if i not in num_set:
            total_sum += i
    if total_sum == 0:
        return ''
    if total_sum % 2:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]