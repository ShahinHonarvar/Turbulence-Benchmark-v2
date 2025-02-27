from index 10 to index 100, both inclusive. If no such integers

def all_ints_div_by_both_two_nums(ints):
    """
    Returns the list of all integers divisible by both 10 and 100
    exist in the specified range, the function should return an empty list.
    """
    return [i for i in ints[10:101] if i % 10 == 0 and i % 100 == 0]