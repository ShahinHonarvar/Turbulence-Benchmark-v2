def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub = s[70:200]
    char_count = {char: sub.count(char) for char in sub if sub.count(char) > 1}
    return ''.join([char for char in s if char not in char_count])