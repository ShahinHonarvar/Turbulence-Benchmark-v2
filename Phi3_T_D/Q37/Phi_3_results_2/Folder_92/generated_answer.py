def filter_chars(s):
    target_range = set(s[4])
    result = [c for c in s if c not in target_range or '7' >= ord(c) >= ord('o')]
    return ''.join(result)