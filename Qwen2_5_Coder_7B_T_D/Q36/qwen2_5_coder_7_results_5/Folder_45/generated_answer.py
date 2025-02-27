def filter_chars(s):
    chars_to_remove = set()
    for i in range(81, 86):
        ch = chr(i)
        if '!' < ch < 's':
            chars_to_remove.add(ch)
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s