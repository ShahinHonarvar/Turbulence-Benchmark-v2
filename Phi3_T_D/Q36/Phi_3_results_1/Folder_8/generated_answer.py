def filter_chars(s):
    start, end = (82, 93)
    chars_to_remove = []
    for i in range(start, end):
        char = s[i]
        if '!' < char < '*':
            chars_to_remove.append(char)
    return ''.join([c for c in s if c not in chars_to_remove])