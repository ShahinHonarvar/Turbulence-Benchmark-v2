def remove_repeat_chars(s):
    chars_to_remove = {char for char in s[86:90] if s.count(char) > 1}
    return ''.join((char if char not in chars_to_remove else '' for char in s))