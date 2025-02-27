def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        is_composite = False
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_composite = True
                break
        if is_composite and 5 <= i <= 7:
            composite_nums.add(num)
    return composite_nums