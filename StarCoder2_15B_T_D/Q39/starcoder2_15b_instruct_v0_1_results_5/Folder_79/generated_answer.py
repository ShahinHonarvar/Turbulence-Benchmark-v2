def return_n_greatest_chars(input_string):
    input_list = list(input_string)
    sorted_list = sorted(input_list, key=lambda x: ord(x), reverse=True)
    return sorted_list[:82]