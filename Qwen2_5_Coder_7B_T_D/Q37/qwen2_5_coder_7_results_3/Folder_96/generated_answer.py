def filter_chars(s):
    chars_to_remove = set()
    for i in range(86, 93):
        char = chr(i)
        if '!' <= char <= 's':
            chars_to_remove.add(char)
    return ''.join((ch for ch in s if ch not in chars_to_remove))