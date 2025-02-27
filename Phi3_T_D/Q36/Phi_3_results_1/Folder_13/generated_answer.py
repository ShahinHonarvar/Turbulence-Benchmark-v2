def filter_chars(s):
    target_chars = [c for c in s[323:526] if ord(c) > ord(')') and ord(c) < ord('O')]
    for c in target_chars:
        s = s.replace(c, '')
    return s