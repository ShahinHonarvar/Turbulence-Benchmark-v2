def return_n_greatest_chars(s):
    sorted_list = sorted(list(s), reverse=True)
    return sorted_list[:76]