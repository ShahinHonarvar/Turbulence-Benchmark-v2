def filter_chars(s):
    result = ''
    for char in s:
        if 32 < ord(char) and ord(char) < 84:
            if ord(char) > ord('m') and ord(char) < ord('w'):
                continue
        result += char
    return result