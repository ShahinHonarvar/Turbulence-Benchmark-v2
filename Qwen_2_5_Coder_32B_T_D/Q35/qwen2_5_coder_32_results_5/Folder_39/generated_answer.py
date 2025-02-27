def remove_repeat_chars(s):
    if len(s) < 92:
        return s
    t = s[45:91]
    counts = {char: t.count(char) for char in set(t) if t.count(char) > 1}
    result = [char for char in s if char not in counts]
    return ''.join(result)