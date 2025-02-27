def return_n_greatest_chars(s):
    sorted_list = sorted(sorted(s), reverse=True)
    return sorted_list[:55]