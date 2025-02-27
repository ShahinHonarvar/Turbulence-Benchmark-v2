def filter_chars(input_str):
    if len(input_str) < 6:
        return input_str
    chars_to_remove = [input_str[i] for i in range(3, 5) if 'Y' < input_str[i] < 's']
    return ''.join((c for c in input_str if c not in chars_to_remove))