def sum_odd_ints_inclusive(ints):
    """Calculate the sum of all odd integers in a list, from index 1 to index 1, both inclusive."""
    return sum((int for int in ints[1:2] if int % 2 == 1))