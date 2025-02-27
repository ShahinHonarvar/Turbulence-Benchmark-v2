def remove_repeat_chars(string):
    for char in set(string[36:85]):
        if string.count(char) > 1:
            string = ''.join([c for c in string if c != char])
    return string