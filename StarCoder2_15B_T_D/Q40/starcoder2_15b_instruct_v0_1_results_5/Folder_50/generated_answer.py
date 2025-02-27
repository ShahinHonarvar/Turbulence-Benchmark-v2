def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    selected_chars = sorted_chars[:16]
    reversed_chars = selected_chars[::-1]
    return reversed_chars