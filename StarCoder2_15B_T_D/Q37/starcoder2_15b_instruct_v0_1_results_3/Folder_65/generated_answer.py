def filter_chars(string):
    for char in string:
        if char.isprintable() and ord(char) in range(61, 71):
            string = string.replace(char, '')
    return string