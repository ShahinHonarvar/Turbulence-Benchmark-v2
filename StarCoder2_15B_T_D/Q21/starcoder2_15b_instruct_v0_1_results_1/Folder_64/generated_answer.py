def all_ints_div_by_num(ints_list):
    """Return a list of all integers divisible by 4 from index 0 to index 0, both inclusive.
    If no such integers exist, return an empty list.

    Args:
        ints_list (list): A list of integers.

    Returns:
        list: A list of all integers divisible by 4 from index 0 to index 0, both inclusive.
    """
    return [num for i, num in enumerate(ints_list) if i >= 0 and i <= 0 and (num % 4 == 0)]