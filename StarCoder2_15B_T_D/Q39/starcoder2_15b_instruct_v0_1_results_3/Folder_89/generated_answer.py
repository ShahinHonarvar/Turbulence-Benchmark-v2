def return_n_greatest_chars(string):
    char_list = list(string)
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)
    sliced_list = sorted_list[:55]
    sorted_list = sorted(sliced_list)
    return sorted_list