def return_n_greatest_chars(input_str):
    sorted_chars = sorted(input_str, key=ord, reverse=True)
    return sorted_chars[:76]