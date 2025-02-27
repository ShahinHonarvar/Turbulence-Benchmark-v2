def remove_repeat_chars(s):
    if len(s) < 8:
        return s
    substr = s[1:7]
    repeat_chars = {char for char in substr if substr.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))