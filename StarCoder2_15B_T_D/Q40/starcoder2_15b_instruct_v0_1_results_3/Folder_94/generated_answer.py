def return_n_smallest_chars(string):
    """
    Returns a list of the 87 characters in `string` that have the smallest ASCII values, sorted in descending order.
    """
    char_list = list(string)
    char_list.sort()
    return char_list[:87][::-1]