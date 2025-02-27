def is_composite(num):
    """
    Check if a number is composite (has more than two factors).
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    """
    Find the set of composite numbers between indices 27 and 55, both inclusive, in a list of positive integers.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 27 <= i <= 55:
            composite_nums.add(num)
    return composite_nums