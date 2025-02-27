def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 88 or i > 90 or (ord(c) < ord('J') or ord(c) > ord('Q')):
            filtered_chars.append(c)
    return ''.join(filtered_chars)