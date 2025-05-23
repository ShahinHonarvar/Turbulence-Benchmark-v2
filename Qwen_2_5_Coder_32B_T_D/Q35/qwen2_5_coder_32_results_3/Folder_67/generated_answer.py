def remove_repeat_chars(s):
    if len(s) <= 67:
        return s
    sub = s[45:67]
    counts = {char: sub.count(char) for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in counts))