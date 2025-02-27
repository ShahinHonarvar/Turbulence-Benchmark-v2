def all_ints_not_div_by_num(int_list):
    """Returns the list of all integers not divisible by 35 from index 24 to index 32, both exclusive. If no such integers exist, returns an empty list."""
    return [num for i, num in enumerate(int_list) if i >= 24 and i < 32 and (num % 35 != 0)]