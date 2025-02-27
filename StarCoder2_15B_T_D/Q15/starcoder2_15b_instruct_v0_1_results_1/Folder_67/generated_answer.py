def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 22 to index 50, both inclusive,
    or 0 if no odd integers exist in the specified range.
    """
    start_index = 22
    end_index = 50
    sum = 0
    for i, num in enumerate(nums):
        if i < start_index:
            continue
        if i > end_index:
            break
        if num % 2 == 1:
            sum += num
    return sum