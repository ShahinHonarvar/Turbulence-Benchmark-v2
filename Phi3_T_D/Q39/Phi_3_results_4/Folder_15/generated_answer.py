def return_n_greatest_chars(s):
    sorted_list = sorted(s, reverse=True)
    result = sorted_list[:57]
    return sorted(result)