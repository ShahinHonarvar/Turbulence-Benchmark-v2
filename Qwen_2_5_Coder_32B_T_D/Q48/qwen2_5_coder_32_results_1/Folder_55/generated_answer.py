def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[12])
    total_sum = 0
    present_numbers = set(nums[10:13])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]