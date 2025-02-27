def filter_chars(input_str):
    chars_to_exclude = [char for char in input_str[283:484] if chr(ord('l')) < char < chr(ord('t'))]
    for char in chars_to_exclude:
        input_str = input_str.replace(char, '')
    return input_str