def filter_chars(string):
    characters_to_remove = set()
    for i, char in enumerate(string):
        if 10 <= i < 15 and ord('t') < ord(char) < ord('v'):
            characters_to_remove.add(char)
    filtered_string = ''
    for char in string:
        if char not in characters_to_remove:
            filtered_string += char
    return filtered_string