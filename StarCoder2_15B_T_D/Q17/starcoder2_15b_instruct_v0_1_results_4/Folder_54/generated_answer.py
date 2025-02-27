def all_ints_div_by_both_two_nums(nums):
    """Returns a list of all integers divisible by both -65 and -62 from index 13 to index 91, both inclusive. If no such integers exist, returns an empty list."""
    return [num for i, num in enumerate(nums) if i >= 13 and i <= 91 and (num % -65 == 0) and (num % -62 == 0)]