def remove_repeat_chars(input_string):
    target_chars = {char for char in input_string[355:988] if input_string.count(char) > 1}
    return ''.join((char for char in input_string if char not in target_chars))