def remove_repeat_chars(string):
    chars_to_remove = {}
    for i, char in enumerate(string):
        if char in string[2:8] and string[2:8].count(char) > 1:
            chars_to_remove[char] = None
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string