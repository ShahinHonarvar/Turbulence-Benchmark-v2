def remove_repeat_chars(s):
    unique_chars = set(s[35:64])
    for char in unique_chars:
        if s.count(char) > 1 and char in s[35:64]:
            s = s.replace(char, '')
    return s