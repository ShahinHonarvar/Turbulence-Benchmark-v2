def filter_chars(input_string):
    filtered_string = [c if (ord(c) < ord('X') or ord(c) > ord('p')) or i < 51 or i > 96 else '' for i, c in enumerate(input_string)]
    return ''.join(filtered_string)