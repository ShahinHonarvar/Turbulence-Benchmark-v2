def filter_chars(s):
    chars_to_remove = set()
    for i in range(54, 84):
        if 54 <= i <= 83 and 'j' <= s[i] <= 'v':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result