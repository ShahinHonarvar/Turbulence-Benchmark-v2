def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[76]
    total_sum = sum(range(a + 1, b)) - sum((nums[i] for i in range(14, 76)))
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')