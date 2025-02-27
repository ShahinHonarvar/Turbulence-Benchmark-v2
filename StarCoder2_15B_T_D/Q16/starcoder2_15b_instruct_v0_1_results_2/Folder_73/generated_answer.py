from index 19 to index 92, both inclusive. If no even integers exist in the

def sum_even_ints_inclusive(lst):
    """
    This function takes a list of integers and returns the sum of all even integers
    specified range, the function returns 0.
    """
    return sum((x for x in lst[19:93] if x % 2 == 0))