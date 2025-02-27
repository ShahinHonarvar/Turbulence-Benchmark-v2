def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 29 and i <= 51:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums