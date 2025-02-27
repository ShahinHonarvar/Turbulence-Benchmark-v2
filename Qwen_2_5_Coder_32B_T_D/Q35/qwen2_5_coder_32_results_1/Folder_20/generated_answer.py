def remove_repeat_chars(s):
    if len(s) <= 97:
        return s
    t = s[27:96]
    counts = {char: t.count(char) for char in set(t) if t.count(char) > 1}
    return ''.join((char for char in s if char not in counts))