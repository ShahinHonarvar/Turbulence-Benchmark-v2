from math import sqrt

def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in the given list `nums` that are between index 0 to index 8, both inclusive.
    If no composite number exists in the specified range, returns an empty set.
    """
    composite_nums = set()
    for num in nums:
        is_composite = False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums