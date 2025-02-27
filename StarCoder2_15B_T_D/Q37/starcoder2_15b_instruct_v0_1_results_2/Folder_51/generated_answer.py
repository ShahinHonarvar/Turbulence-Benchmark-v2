def filter_chars(string):
    chars_to_remove = set()
    for i, char in enumerate(string):
        if 36 <= i <= 40 and ord('H') <= ord(char) <= ord('e'):
            chars_to_remove.add(char)
    filtered_string = ''
    for char in string:
        if char not in chars_to_remove:
            filtered_string += char
    return filtered_string