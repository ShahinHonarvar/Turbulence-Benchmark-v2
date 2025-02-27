def filter_chars(string):
    chars_to_remove = []
    for i, char in enumerate(string):
        if i >= 283 and i < 484 and (ord(char) > ord('l')) and (ord(char) < ord('t')):
            chars_to_remove.append(char)
    return ''.join([char for char in string if char not in chars_to_remove])