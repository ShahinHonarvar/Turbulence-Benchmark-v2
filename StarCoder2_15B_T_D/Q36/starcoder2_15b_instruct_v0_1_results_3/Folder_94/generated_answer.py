def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 15 or i >= 85:
            filtered_chars.append(c)
        elif not ord('I') < ord(c) < ord('M'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)