def all_even_ints_inclusive(nums):
    """
    Takes a list of integers and returns the list of all even integers from index 55 to index 98, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_nums = []
    for i, num in enumerate(nums):
        if i >= 55 and i <= 98 and (num % 2 == 0):
            even_nums.append(num)
    return even_nums