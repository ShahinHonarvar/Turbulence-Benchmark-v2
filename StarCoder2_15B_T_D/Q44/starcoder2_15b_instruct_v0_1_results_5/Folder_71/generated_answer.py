import math

def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in 'nums' between index 59 and 97, both inclusive.
    If no composite number exists in the specified range, returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i < 59 or i > 97:
            continue
        is_composite = False
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums