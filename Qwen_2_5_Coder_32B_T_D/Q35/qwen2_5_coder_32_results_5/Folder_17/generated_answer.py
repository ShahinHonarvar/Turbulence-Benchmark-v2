def remove_repeat_chars(s):
    if len(s) <= 84:
        return s
    sub = s[74:83]
    counts = {char: sub.count(char) for char in sub}
    repeated_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))