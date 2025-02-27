def remove_repeat_chars(s):
    if len(s) < 202:
        return s
    chars_to_remove = {char for char in s[20:200] if s[20:200].count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove or not 20 <= s.index(char) <= 200))