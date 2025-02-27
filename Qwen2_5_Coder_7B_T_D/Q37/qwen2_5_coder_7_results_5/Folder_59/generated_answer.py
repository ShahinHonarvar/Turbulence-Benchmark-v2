def filter_chars(s):
    chars_to_remove = set()
    for i in range(2, 4):
        if '5' <= s[i] <= '_':
            chars_to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in chars_to_remove))