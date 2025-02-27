def composite_nums_between_indices(lst):
    """
    Returns the set of all composite numbers in the given list that are between
    index 222 to index 222, both inclusive. If no composite number exists in the
    specified range, returns an empty set.
    """

    def is_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    composite_nums = set()
    for i, num in enumerate(lst):
        if i >= 222 and i <= 222 and is_composite(num):
            composite_nums.add(num)
    return composite_nums