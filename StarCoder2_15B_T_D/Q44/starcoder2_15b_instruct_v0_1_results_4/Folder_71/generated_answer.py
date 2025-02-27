def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 59 and i <= 97:
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    composite_nums.add(num)
                    break
    return composite_nums