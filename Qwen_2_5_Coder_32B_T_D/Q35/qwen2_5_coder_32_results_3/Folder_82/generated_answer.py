def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    sub = s[30:201]
    counts = {char: sub.count(char) for char in set(sub)}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))