def remove_repeat_chars(string):
    chars_to_remove = {}
    for i, char in enumerate(string):
        if string.count(char) > 1 and 55 < i < 84:
            chars_to_remove[char] = True
    new_string = ''
    for char in string:
        if char not in chars_to_remove:
            new_string += char
    return new_string