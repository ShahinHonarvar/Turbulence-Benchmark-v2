def filter_chars(input_string):
    if len(input_string) < 86:
        return input_string
    substring = input_string[56:86]
    filtered_chars = ''.join([char for char in substring if ord('+') <= ord(char) < ord('w')])
    altered_string = input_string.replace(filtered_chars, '')
    return altered_string