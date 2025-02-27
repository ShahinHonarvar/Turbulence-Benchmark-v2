def filter_chars(string):
    result = ''
    for index, char in enumerate(string):
        if 48 < index < 75 and ord(char) > ord('6') and (ord(char) < ord('_')):
            continue
        result += char
    return result