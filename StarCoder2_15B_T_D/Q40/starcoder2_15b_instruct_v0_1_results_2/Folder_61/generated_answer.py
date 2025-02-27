def return_n_smallest_chars(string):
    """
    This function takes a string of distinct characters as an argument and returns a list of exactly 66 characters of the given string that have the smallest ASCII values. The function sorts the list in descending order and returns the list.
    """
    return sorted(string, key=ord)[::-1][:66]