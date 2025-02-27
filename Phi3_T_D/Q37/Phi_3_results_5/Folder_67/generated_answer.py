def filter_chars(input_string):
    selected_chars = set(input_string[19:23])
    for char in selected_chars:
        if ']' <= char <= 't':
            input_string = input_string.replace(char, '')
    return input_string