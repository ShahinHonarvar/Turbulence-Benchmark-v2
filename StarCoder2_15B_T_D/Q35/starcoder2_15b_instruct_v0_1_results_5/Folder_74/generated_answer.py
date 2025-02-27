def remove_repeat_chars(string):
    char_to_remove = []
    for i, char in enumerate(string):
        if char in string[69:97] and string[69:97].count(char) > 1:
            char_to_remove.append(char)
    for char in char_to_remove:
        string = string.replace(char, '')
    return string