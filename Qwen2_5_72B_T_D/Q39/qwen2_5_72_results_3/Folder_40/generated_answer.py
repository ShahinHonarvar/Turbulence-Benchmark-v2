def return_n_greatest_chars(s):
    char_list = [char for char in s]
    char_list.sort(reverse=True)
    return char_list[:7]