def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 6 and i <= 6:
            if num > 1:
                for divisor in range(2, num):
                    if num % divisor == 0:
                        composite_nums.add(num)
                        break
    return composite_nums