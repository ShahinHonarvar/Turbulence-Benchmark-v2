def all_ints_div_by_num(nums):
    """
    Returns the list of all integers divisible by 77 from index 66 to index 81, both inclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(nums):
        if i >= 66 and i <= 81 and (num % 77 == 0):
            result.append(num)
    return result