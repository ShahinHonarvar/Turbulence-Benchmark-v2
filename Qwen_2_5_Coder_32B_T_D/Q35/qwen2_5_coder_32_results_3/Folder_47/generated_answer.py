def remove_repeat_chars(s):
    if len(s) <= 53:
        return s
    segment = s[30:53]
    counts = {char: segment.count(char) for char in set(segment)}
    remove_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in remove_chars))