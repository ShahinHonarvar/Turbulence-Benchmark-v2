def remove_repeat_chars(string):
    for char in string:
        if string.count(char) > 1 and 50 < string.index(char) < 200:
            string = string.replace(char, '')
    return string