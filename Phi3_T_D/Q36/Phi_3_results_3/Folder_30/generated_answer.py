def filter_chars(s):
    char = chr((ord('3') + ord('I')) // 2)
    parts = [s[:23] + s[45:], ''.join(filter(lambda c: c != char, s[23:45]))]
    return ''.join(parts)