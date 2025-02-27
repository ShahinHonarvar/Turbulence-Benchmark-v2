def return_n_smallest_chars(string):
    char_list = sorted(string)
    smallest_chars_54 = char_list[:-54]
    return sorted(smallest_chars_54, reverse=True)