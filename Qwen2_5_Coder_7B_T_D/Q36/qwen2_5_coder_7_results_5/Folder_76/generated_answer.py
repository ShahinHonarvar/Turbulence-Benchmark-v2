def filter_chars(s):
    chars_to_remove = set()
    for i in range(669, 888):
        char = s[i]
        if 'B' < char < 'Y':
            chars_to_remove.add(char)
    result = ''.join((ch for ch in s if ch not in chars_to_remove))
    return result