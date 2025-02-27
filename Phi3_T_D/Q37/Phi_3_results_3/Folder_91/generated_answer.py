def filter_chars(input_str):
    char_to_filter = input_str[6] if len(input_str) > 6 else ''
    if 'B' <= char_to_filter <= 'H':
        return input_str.replace(char_to_filter, '')
    return input_str