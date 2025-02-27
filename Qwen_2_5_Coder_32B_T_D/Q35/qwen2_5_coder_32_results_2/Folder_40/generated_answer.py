def remove_repeat_chars(s):
    target = s[1:4]
    counts = {char: target.count(char) for char in set(target)}
    return ''.join((char for char in s if counts.get(char, 1) == 1))