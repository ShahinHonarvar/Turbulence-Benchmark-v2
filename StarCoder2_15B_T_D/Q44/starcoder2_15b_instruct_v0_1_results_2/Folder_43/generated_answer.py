def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in `nums` between index 31 and index 72, both inclusive.
    If no composite number exists in the specified range, returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if num > 1 and i >= 31 and (i <= 72):
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums