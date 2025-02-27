def remove_repeat_chars(s):
    if len(s) <= 64:
        return s
    target = s[36:64]
    counts = {char: target.count(char) for char in target}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))