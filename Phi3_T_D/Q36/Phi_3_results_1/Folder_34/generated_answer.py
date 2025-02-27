def filter_chars(s):
    if len(s) < 90:
        return s
    for char_code in range(ord('?') + 1, ord('m')):
        s = s.replace(chr(char_code), '')
    return s