def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in the given list `nums` that are between index 13 and index 68, both inclusive.
    If no composite number exists in the specified range, returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 13 and i <= 68:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(num):
    """
    Returns True if `num` is a composite number, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False