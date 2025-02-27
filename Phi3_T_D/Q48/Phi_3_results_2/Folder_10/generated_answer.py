def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    missing_sum = sum(set(range(a + 1, b)).difference(set(nums[a + 1:b + 1])))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')