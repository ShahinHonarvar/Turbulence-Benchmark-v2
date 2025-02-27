def filter_chars(string):
    for i, char in enumerate(string):
        if 19 <= i <= 22 and ord(char) in range(ord(']'), ord('t') + 1):
            string = string.replace(char, '')
    return string