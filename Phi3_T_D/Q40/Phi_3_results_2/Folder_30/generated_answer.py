def return_n_smallest_chars(input_string):
    if len(input_string) < 72:
        return sorted(input_string)
    else:
        return sorted(input_string)[:72]