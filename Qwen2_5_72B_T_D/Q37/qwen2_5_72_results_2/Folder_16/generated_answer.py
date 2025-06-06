def filter_chars(s):
    chars_to_remove = set()
    for i in range(225, 382):
        if 225 <= i <= 381 and 'D' <= s[i] <= 'Y':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result