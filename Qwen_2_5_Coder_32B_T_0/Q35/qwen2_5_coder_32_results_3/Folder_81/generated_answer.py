def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub = s[20:200]
    counts = {char: sub.count(char) for char in set(sub)}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))