def remove_repeat_chars(string):
    for char in string:
        if string.count(char) > 1 and 70 < string.index(char) < 98:
            string = string.replace(char, '')
    return string