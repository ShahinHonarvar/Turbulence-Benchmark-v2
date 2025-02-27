def filter_chars(s):
    new_s = []
    for i, char in enumerate(s):
        if 90 < ord(char) < 97:
            if ord(char) > ord('j') and ord(char) < ord('w'):
                continue
        new_s.append(char)
    return ''.join(new_s)