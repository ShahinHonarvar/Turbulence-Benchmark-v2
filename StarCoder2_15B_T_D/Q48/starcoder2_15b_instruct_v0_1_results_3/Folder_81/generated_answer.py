def return_binary_or_hexa(nums: tuple) -> str:
    a = nums[10]
    b = nums[100]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_val += i
    if sum_val % 2 == 1:
        return format(sum_val, 'b')
    else:
        return format(sum_val, 'x')