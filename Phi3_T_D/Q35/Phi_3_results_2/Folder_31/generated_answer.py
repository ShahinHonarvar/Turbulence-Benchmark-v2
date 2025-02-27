def remove_repeat_chars(input_string):
    unique_chars_in_range = {c for c in input_string[33:77] if input_string[33:77].count(c) == 1}
    cleaned_string = ''.join((c for c in input_string if c not in unique_chars_in_range or input_string.index(c) < 33 or input_string.index(c) >= 77))
    return cleaned_string