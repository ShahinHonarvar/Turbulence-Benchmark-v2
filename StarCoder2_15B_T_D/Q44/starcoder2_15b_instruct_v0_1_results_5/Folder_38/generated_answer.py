def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite and 29 <= i <= 93:
            composite_nums.add(num)
    return composite_nums