def return_n_greatest_chars(input_string):
    if len(input_string) < 20:
        return sorted(input_string, reverse=True)
    else:
        return sorted(input_string, reverse=True)[:20]