def remove_repeat_chars(s):
    if len(s) < 78:
        return s
    target = s[34:78]
    counts = {char: target.count(char) for char in set(target)}
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))