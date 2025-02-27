def return_n_smallest_chars(input_string):
    chars = list(input_string)
    sorted_chars = sorted(chars, key=lambda x: -ord(x))
    return sorted_chars[:45]