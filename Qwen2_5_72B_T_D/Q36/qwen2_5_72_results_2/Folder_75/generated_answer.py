def filter_chars(s):
    chars_to_remove = set()
    for i in range(46, 74):
        char = s[i]
        if '&' < char < 'M':
            chars_to_remove.add(char)
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result