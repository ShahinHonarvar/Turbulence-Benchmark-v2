def composite_nums_between_indices(nums):
    """
    This function takes a list of positive integers as input and returns the set of
    composite numbers between index 30 and index 30, both inclusive. If no composite
    number exists in the specified range, an empty set is returned.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 30 and i <= 30:
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums