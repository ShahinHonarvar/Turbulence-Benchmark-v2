def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    sub = s[45:78]
    counts = {char: sub.count(char) for char in sub if sub.count(char) > 1}
    result = [char for char in s if char not in counts]
    return ''.join(result)