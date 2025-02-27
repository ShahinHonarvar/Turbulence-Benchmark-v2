def composite_nums_between_indices(nums):
    """
    Return the set of all composite numbers in the given list that are between index 262 and index 746, both inclusive.
    If no composite number exists in the specified range, return an empty set.
    """

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 262 <= i <= 746:
            result.add(num)
    return result