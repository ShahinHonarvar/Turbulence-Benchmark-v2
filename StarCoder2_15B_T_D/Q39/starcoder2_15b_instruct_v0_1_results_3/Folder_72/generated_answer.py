def return_n_greatest_chars(string):
    """
    Create the sorted list of exactly 37 characters of the given string that have the greatest ASCII values.
    Sort the list in descending order and return it.
    """
    sorted_chars = sorted(string, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:37]