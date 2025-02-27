def all_pos_ints_inclusive(lst):
    """
    <Write a function called 'all_pos_ints_inclusive' that takes one argument, a list of integers, and returns the list of all positive integers from index 75 to index 94, both inclusive. If no positive integers exist in the specified range, the function should return an empty list.>
    """
    pos_ints = [x for x in lst[75:95] if x > 0]
    return pos_ints