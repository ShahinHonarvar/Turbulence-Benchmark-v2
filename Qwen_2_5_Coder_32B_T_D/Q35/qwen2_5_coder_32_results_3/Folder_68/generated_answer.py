def remove_repeat_chars(s):
    t = s[1:10]
    counts = {char: t.count(char) for char in set(t)}
    return ''.join((char for char in s if counts.get(char, 1) == 1))