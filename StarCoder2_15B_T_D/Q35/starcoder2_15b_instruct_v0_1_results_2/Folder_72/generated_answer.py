def remove_repeat_chars(string):
    chars = [c for c in string[13:70] if string[13:70].count(c) > 1]
    for char in chars:
        string = string.replace(char, '')
    return string