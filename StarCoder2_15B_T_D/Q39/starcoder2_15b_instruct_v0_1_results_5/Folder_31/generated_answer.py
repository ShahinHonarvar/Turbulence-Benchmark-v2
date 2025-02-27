def return_n_greatest_chars(input_string):
    input_list = list(input_string)
    input_list.sort(key=lambda x: ord(x), reverse=True)
    return input_list[:70]