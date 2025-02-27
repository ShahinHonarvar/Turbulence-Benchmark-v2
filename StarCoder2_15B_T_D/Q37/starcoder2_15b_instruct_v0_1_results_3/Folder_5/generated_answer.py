def filter_chars(input_string):
    filtered_chars = [char for i, char in enumerate(input_string) if (i < 24 or i > 82) or not (ord(char) >= ord('5') and ord(char) <= ord('<'))]
    return ''.join(filtered_chars)