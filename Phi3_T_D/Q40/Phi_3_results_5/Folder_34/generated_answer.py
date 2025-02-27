def return_n_smallest_chars(s):
    sorted_list = sorted(s)
    smallest_9 = sorted_list[:9]
    return sorted(smallest_9, reverse=True)