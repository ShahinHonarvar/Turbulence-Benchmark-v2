def filter_chars(s):
    chars = list(s)
    for i in range(3, 9):
        if ord(chars[i]) > ord('*') and ord(chars[i]) < ord('E'):
            chars = [c for c in chars if c != chars[i]]
    return ''.join(chars)