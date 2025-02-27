def remove_repeat_chars(s):
    sub = s[2:7]
    counts = {char: sub.count(char) for char in set(sub)}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))