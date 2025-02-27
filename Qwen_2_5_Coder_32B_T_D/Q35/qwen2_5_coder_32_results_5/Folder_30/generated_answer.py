def remove_repeat_chars(s):
    if len(s) <= 24:
        return s
    sub = s[23:24]
    counts = {char: s.count(char) for char in sub}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))