def return_n_greatest_chars(input_string):
    if len(input_string) < 54:
        return []
    sorted_chars = sorted(input_string, reverse=True)
    return sorted_chars[:54]