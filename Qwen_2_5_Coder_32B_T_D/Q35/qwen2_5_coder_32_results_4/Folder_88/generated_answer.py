def remove_repeat_chars(s):
    t = s[4:9]
    counts = {char: t.count(char) for char in t}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))