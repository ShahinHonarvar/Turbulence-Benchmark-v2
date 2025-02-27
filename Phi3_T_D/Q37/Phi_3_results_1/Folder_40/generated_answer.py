def filter_chars(s):
    if not s or s[0] < '*' or s[1] > 's':
        return s
    target_char = chr(ord(s[0]) + 1)
    while target_char <= s[1]:
        s = s.replace(target_char, '')
        target_char = chr(ord(target_char) + 1)
    return s