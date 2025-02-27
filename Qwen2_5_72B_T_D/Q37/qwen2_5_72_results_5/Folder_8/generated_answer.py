def filter_chars(s):
    chars_to_remove = set()
    for i in range(41, 87):
        if 41 <= i <= 86 and 'S' <= s[i] <= 's':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result