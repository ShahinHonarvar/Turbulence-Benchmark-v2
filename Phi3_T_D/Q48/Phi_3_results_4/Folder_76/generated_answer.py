def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    sum_of_missing_nums = sum((n for n in range(a + 1, b) if n not in nums[450:906]))
    if sum_of_missing_nums % 2 == 0:
        return '{:x}'.format(sum_of_missing_nums)
    else:
        return bin(sum_of_missing_nums)[2:]