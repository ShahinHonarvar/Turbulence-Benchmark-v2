def composite_nums_between_indices(nums):
    """
    Return the set of all composite numbers in the given list that are between index 29 to index 79, both inclusive.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i < 29 or i > 79:
            continue
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums