def composite_nums_between_indices(nums):
    """
    Finds the set of all composite numbers in the given list that are between index 533 to index 605, both inclusive.
    If no composite number exists in the specified range, returns an empty set.
    """
    all_composite_nums = {n for n in range(1, max(nums) + 1) if not all((n % i for i in range(2, int(n ** 0.5) + 1)))}
    return {n for n in all_composite_nums if 533 <= nums.index(n) <= 605}