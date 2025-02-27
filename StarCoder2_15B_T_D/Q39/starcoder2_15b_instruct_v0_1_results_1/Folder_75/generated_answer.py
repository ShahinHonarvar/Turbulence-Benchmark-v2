def return_n_greatest_chars(chars):
    char_list = list(chars)
    char_list.sort(key=lambda c: ord(c), reverse=True)
    return sorted(char_list[:2])