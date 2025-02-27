def composite_nums_between_indices(nums):
    """
    Find composite numbers between indices 22 and 63 in a list of integers.

    Args:
        nums (list): A list of positive integers.

    Returns:
        set: A set of composite numbers between indices 22 and 63, or an empty set if no composite number exists.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 22 and i <= 63:
            is_composite = False
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(num)
    return composite_nums