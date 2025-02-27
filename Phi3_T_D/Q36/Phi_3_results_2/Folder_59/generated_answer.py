def filter_chars(input_string):
    if len(input_string) < 8:
        return input_string
    char_to_remove = None
    for char in input_string[3:8]:
        if '?' < char < 'k':
            char_to_remove = char
            break
    if char_to_remove:
        return input_string.replace(char_to_remove, '')
    return input_string