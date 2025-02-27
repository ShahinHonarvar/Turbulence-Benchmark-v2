def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    composite_nums_in_range = set()
    for num in composite_nums:
        if 62 <= nums.index(num) <= 78:
            composite_nums_in_range.add(num)
    return composite_nums_in_range