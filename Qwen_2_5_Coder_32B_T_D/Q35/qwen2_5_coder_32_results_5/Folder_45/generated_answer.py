def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    t = s[40:200]
    to_remove = {char for char in t if t.count(char) > 1}
    return ''.join([char for char in s if char not in to_remove])