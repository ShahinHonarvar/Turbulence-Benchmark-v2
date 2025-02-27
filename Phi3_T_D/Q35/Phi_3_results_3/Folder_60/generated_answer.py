def remove_repeat_chars(s):
    unique_chars = set()
    substr = s[38:52]
    for char in substr:
        if substr.count(char) > 1:
            s = s.replace(char, '', s.count(char))
    return s