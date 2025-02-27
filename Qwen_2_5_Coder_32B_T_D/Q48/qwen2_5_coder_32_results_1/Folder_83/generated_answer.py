def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[200]
    total_sum = 0
    present_numbers = set(nums[91:200])
    for i in range(a + 1, b):
        if i not in present_numbers:
            total_sum += i
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]