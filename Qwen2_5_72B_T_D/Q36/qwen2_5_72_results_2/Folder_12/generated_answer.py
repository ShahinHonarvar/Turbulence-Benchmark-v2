def filter_chars(s):
    result = ''
    for char in s:
        if not (32 < ord(char) < 84 and 'm' < char < 'w'):
            result += char
    return result