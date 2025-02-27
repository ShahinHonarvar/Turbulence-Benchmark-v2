def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in 'nums' that are between index 82
    and index 86, both inclusive. If no composite number exists in the specified range,
    returns an empty set.
    """
    return {num for i, num in enumerate(nums) if i >= 82 and i <= 86 and (num > 1) and (not all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))))}