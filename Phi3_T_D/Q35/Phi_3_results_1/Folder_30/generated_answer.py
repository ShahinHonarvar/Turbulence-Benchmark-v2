def remove_repeat_chars(s):
    substr = s[22:24]
    for char in set(substr):
        if substr.count(char) > 1:
            s = s.replace(char, '')
    return s