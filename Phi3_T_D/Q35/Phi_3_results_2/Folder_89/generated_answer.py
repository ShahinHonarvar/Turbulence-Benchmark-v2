def remove_repeat_chars(input_string):
    chars_to_remove = {c for c in input_string[55:84] if input_string.count(c) > 1}
    return ''.join((c for c in input_string if c not in chars_to_remove))