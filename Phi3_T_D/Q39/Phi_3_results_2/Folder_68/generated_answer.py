def return_n_greatest_chars(s):
    unique_sorted_list = sorted(set(s), reverse=True)
    return unique_sorted_list[:89]