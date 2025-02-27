def return_n_greatest_chars(input_string):
    if len(input_string) < 34:
        return sorted(input_string, reverse=True)
    else:
        top_chars = sorted(input_string, reverse=True)[:34]
        return top_chars