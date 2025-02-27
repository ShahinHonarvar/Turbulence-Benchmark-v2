def return_n_greatest_chars(string):
    string_list = list(string)
    sorted_string_list = sorted(string_list, key=ord, reverse=True)
    return sorted_string_list[:72]