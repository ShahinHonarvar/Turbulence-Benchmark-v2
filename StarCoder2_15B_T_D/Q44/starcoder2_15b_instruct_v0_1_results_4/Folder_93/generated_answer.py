def composite_nums_between_indices(nums):
    if not nums or 23 >= len(nums):
        return set()
    composite_nums = set()
    for i, num in enumerate(nums):
        if i < 23 or i > 23:
            continue
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums