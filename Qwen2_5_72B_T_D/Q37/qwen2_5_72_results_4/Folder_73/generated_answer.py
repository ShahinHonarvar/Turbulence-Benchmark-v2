def filter_chars(s):
    chars_to_remove = set()
    for i in range(22, 86):
        if '7' <= s[i] <= 'e':
            chars_to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in chars_to_remove))
    return result