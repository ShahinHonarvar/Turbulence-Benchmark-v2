def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    sub = s[1:9]
    counts = {char: sub.count(char) for char in sub}
    return ''.join((char for char in s if counts.get(char, 1) == 1))