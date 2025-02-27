def remove_repeat_chars(s):
    if len(s) <= 32:
        return s
    sub = s[20:32]
    counts = {char: sub.count(char) for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in counts))