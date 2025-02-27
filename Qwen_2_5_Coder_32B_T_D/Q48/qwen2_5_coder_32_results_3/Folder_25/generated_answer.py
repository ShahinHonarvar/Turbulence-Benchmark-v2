def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    total_sum = 0
    present_numbers = set(nums[38:43])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]