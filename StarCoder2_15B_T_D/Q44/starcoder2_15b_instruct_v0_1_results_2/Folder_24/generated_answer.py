def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in the given list that are between index 34 to index 55, both inclusive. If no composite number exists in the specified range, returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 34 and i <= 55:
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums