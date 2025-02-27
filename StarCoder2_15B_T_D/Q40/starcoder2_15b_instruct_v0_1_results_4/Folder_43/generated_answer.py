def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    selected_chars = sorted_chars[:56][::-1]
    return list(selected_chars)