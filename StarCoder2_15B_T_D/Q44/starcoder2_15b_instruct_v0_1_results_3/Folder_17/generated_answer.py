def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 50 and i <= 54:
            for divisor in range(2, num):
                if num % divisor == 0:
                    composite_nums.add(num)
                    break
    return composite_nums