def all_ints_not_div_by_num(nums):
    """
    Returns the list of all integers not divisible by 90 from index 48 to index 92,
    both exclusive. If no such integers exist in the specified range, the function
    should return an empty list.
    """
    result = []
    for i, num in enumerate(nums):
        if i < 48 or i >= 92:
            continue
        if num % 90 != 0:
            result.append(num)
    return result