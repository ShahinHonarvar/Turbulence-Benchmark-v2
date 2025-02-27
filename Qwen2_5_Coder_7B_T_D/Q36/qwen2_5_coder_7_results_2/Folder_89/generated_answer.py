def filter_chars(s):
    chars_to_remove = set()
    for i in range(57, 69):
        char = chr(i)
        if '(' < char < 'W':
            chars_to_remove.add(char)
    return ''.join((ch for ch in s if ch not in chars_to_remove))