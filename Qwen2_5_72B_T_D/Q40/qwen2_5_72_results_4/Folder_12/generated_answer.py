def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_61 = sorted_chars[:61]
    return smallest_61[::-1]