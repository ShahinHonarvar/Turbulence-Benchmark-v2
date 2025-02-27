def filter_chars(input_string):
    allowed_range = [ord(char) for char in input_string[35:60] if '!' < char < 'B']
    chars_to_remove = set(input_string) - set('!' + ''.join((chr(code) for code in allowed_range)))
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result