def all_ints_div_by_both_two_nums(nums):
    """
    Returns the list of all integers divisible by both -24 and -11 from index 55 to index 84, both inclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(nums):
        if i >= 55 and i <= 84 and (num % -24 == 0) and (num % -11 == 0):
            result.append(num)
    return result