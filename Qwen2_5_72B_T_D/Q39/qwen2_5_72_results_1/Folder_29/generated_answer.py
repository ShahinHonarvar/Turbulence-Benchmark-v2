def return_n_greatest_chars(s):
    if len(s) < 23:
        return []
    else:
        char_list = list(s)
        sorted_list = sorted(char_list, reverse=True)
        return sorted_list[:23]