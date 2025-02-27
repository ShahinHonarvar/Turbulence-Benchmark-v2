def filter_chars(string):
    chars_to_remove = []
    for i, char in enumerate(string):
        if 21 < i < 25 and ord('5') < ord(char) < ord('}'):
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string