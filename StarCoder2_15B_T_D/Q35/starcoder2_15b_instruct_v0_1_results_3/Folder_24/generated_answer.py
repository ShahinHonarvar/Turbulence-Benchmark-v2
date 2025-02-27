def remove_repeat_chars(string):
    chars_to_remove = {}
    for i, char in enumerate(string[13:91]):
        if char in string[13:i]:
            chars_to_remove[char] = True
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string