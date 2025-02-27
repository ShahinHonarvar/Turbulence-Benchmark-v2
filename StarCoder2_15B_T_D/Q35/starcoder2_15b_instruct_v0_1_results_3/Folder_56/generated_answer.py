def remove_repeat_chars(string):
    for char in string:
        if string.count(char) > 1 and 7 < string.index(char) < 9:
            string = ''.join([c for c in string if c != char])
    return string