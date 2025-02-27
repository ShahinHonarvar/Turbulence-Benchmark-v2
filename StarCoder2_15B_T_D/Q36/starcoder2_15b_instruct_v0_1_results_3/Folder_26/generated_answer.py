def filter_chars(string):
    chars_to_remove = []
    for i, char in enumerate(string):
        if 43 < i < 83 and ':' < char < 'Q':
            chars_to_remove.append(char)
    return ''.join([char for char in string if char not in chars_to_remove])