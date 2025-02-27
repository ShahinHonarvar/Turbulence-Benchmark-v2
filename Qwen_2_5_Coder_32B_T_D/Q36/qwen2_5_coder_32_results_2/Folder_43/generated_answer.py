def filter_chars(s):
    if len(s) <= 75:
        return s
    chars_to_remove = set()
    for char in s[27:75]:
        if 'A' < char < 'i':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))