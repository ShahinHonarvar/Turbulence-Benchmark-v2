def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in 'nums' that are between index 15 and index 39, both inclusive.
    If no composite number exists in the specified range, returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i < 15 or i > 39:
            continue
        if num < 2:
            continue
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums