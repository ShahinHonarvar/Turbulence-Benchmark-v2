def remove_repeat_chars(s):
    if len(s) < 201:
        return s
    t = s[30:200]
    charsToRemove = {char for char in t if t.count(char) > 1}
    return ''.join([char for char in s if char not in charsToRemove])