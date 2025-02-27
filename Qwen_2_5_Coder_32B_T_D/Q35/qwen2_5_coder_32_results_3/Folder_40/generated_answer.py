def remove_repeat_chars(s):
    t = s[1:4]
    counts = {char: t.count(char) for char in t}
    return ''.join((char for char in s if char not in [k for k, v in counts.items() if v > 1]))