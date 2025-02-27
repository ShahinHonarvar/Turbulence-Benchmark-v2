def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in `nums` that are between index 37 and index 76, both inclusive.
    If no composite number exists in the specified range, returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if num > 1 and i >= 37 and (i <= 76):
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums