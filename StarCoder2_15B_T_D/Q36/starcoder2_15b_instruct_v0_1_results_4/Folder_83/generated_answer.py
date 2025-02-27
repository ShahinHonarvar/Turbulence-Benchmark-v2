def filter_chars(s):
    chars_to_remove = set()
    for i in range(72, 93):
        if chr(i) > '<' and chr(i) < 'J':
            chars_to_remove.add(chr(i))
    filtered_chars = []
    for c in s:
        if c not in chars_to_remove:
            filtered_chars.append(c)
    return ''.join(filtered_chars)