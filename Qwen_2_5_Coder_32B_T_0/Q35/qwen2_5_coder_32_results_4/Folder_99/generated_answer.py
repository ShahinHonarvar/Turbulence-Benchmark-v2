def remove_repeat_chars(s):
    if len(s) <= 905:
        return s
    sub = s[451:905]
    counts = {char: sub.count(char) for char in set(sub) if sub.count(char) > 1}
    return ''.join((char for char in s if char not in counts))