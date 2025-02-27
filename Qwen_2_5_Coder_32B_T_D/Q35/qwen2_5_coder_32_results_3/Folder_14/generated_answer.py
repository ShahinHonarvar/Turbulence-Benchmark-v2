def remove_repeat_chars(s):
    t = s[3:5]
    counts = {char: t.count(char) for char in set(t)}
    return ''.join((char for char in s if counts.get(char, 1) == 1 or char not in counts))