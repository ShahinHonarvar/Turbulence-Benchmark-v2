def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if num > 1 and any((num % j == 0 for j in range(2, num))):
            if 3 <= i <= 5:
                composite_nums.add(num)
    return composite_nums