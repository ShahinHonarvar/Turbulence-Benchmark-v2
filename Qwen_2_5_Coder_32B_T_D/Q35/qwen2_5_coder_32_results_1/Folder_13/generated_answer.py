def remove_repeat_chars(s):
    start, end = (46, 91)
    if len(s) <= end:
        return s
    target = s[start:end]
    counts = {char: target.count(char) for char in set(target) if target.count(char) > 1}
    return ''.join((char for char in s if char not in counts))