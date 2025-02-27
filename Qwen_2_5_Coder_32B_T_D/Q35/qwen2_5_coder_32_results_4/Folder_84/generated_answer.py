def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    target = s[33:44]
    counts = {char: target.count(char) for char in set(target)}
    repeat_chars = {char for char, cnt in counts.items() if cnt > 1}
    return ''.join((char for char in s if char not in repeat_chars))