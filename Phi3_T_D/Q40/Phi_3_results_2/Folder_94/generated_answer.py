def return_n_smallest_chars(s):
    unique_chars = list(s)
    unique_chars.sort()
    smallest_chars = unique_chars[:87]
    smallest_chars.sort(reverse=True)
    return smallest_chars