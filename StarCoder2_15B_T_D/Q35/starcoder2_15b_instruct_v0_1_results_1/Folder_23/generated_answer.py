def remove_repeat_chars(string):
    chars_to_remove = set()
    for i, char in enumerate(string):
        if string.count(char) > 1 and 20 < i < 36:
            chars_to_remove.add(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string