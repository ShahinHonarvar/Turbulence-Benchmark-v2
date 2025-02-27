def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            total_sum += i
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')