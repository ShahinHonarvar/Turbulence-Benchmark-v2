def remove_repeat_chars(s):
    if len(s) <= 85:
        return s
    sub = s[37:85]
    counts = {char: sub.count(char) for char in set(sub) if sub.count(char) > 1}
    return ''.join((char for char in s if char not in counts))