def return_n_greatest_chars(input_string):
    if len(input_string) < 43:
        return 'Input string must contain at least 43 distinct characters.'
    if len(set(input_string)) > 43:
        input_string = set(input_string)
    return sorted(list(input_string), key=ord, reverse=True)[:43]