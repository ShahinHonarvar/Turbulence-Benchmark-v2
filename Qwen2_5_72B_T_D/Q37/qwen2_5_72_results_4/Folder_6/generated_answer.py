def filter_chars(s):
    chars_to_remove = set()
    for i in range(13, 29):
        if 'c' <= s[i] <= 'n':
            chars_to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in chars_to_remove))
    return result