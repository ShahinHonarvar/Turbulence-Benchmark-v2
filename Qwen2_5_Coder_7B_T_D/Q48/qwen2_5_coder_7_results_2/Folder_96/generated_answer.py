def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[200]
    total = sum(range(a + 1, b))
    missing = sum((num for num in range(a + 1, b) if num not in nums[50:201]))
    if missing % 2 == 0:
        return format(missing, 'x')
    else:
        return format(missing, 'b')