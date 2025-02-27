def return_n_greatest_chars(string):
    chars_list = list(string)
    sorted_chars_list = sorted(chars_list, key=lambda c: ord(c), reverse=True)
    return sorted_chars_list[:37]