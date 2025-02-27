def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    target = s[1:9]
    counts = {char: target.count(char) for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in counts))