def return_binary_or_hexa(nums):
    a = nums[11]
    b = nums[76]
    sum_missing = sum((i for i in range(a + 1, b) if i not in nums[11:77]))
    num_missing_even = sum((1 for i in nums if nums.count(i) == 0))
    return format(sum_missing, 'b') if num_missing_even % 2 == 0 else format(sum_missing, 'x')