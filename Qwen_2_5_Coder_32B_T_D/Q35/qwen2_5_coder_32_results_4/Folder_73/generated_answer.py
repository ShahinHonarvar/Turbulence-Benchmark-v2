def remove_repeat_chars(s):
    sub = s[11:76]
    char_count = {char: sub.count(char) for char in set(sub) if sub.count(char) > 1}
    return ''.join((c for c in s if c not in char_count))