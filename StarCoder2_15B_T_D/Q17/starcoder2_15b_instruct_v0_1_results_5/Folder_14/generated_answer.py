def all_ints_div_by_both_two_nums(ints_list):
    """
    Returns a list of integers divisible by both 2 and 3 from index 7 to index 9, both inclusive.
    If no such integers exist, an empty list is returned.
    """
    return [i for i in ints_list[7:10] if i % 2 == 0 and i % 3 == 0]