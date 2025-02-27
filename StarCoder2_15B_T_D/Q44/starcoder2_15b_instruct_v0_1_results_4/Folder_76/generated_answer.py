def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in the given list that are between index 639 to index 975, both inclusive.
    If no composite number exists in the specified range, an empty set is returned.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 639 and i <= 975:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(num):
    """Checks if a given number is composite."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False