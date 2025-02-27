def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i < 309 or i >= 591:
            result += char
        elif not (ord(char) > ord('S') and ord(char) < ord('m')):
            result += char
    return result