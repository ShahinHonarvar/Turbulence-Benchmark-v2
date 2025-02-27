def remove_repeat_chars(s):
    tailored_chars = s[46:91]
    filtered_chars = ''.join((c for i, c in enumerate(s) if c not in tailored_chars or s.index(c) not in range(46, 91)))
    return filtered_chars