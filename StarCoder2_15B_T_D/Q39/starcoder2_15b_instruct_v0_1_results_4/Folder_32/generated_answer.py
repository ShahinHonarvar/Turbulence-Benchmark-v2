def return_n_greatest_chars(characters):
    char_list = list(characters)
    sorted_list = sorted(char_list, key=ord, reverse=True)
    return sorted_list[:8]