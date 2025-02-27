def remove_repeat_chars(s):
    if len(s) <= 74:
        return s
    target = s[50:74]
    counts = {char: target.count(char) for char in set(target) if target.count(char) > 1}
    return ''.join((char for char in s if char not in counts))