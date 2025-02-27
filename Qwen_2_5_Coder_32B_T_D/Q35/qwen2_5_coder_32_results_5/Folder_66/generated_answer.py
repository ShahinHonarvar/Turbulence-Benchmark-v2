def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    sub = s[12:76]
    counts = {char: sub.count(char) for char in set(sub) if sub.count(char) > 1}
    res = ''.join([char for char in s if char not in counts])
    return res