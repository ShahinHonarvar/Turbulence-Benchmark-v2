def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, reverse=True)[:46]
    sorted_chars.sort()
    return sorted_chars