def filter_chars(text):
    chars_to_remove = set()
    for i in range(29, 33):
        if chr(i) > '%' and chr(i) < 'a':
            chars_to_remove.add(chr(i))
    result = ''
    for c in text:
        if c not in chars_to_remove:
            result += c
    return result