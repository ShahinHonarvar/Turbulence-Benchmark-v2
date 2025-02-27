def return_n_greatest_chars(input_string):
    sorted_list = sorted(input_string, key=ord, reverse=True)
    return sorted_list[:85]