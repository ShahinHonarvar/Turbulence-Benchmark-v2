def filter_chars(input_string):
    filtered_string = ''.join([char for i, char in enumerate(input_string) if not (29 <= i <= 97 and '-' <= char <= 'n')])
    return filtered_string