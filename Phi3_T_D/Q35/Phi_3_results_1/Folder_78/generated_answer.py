def remove_repeat_chars(s):
    chars_to_remove = [char for char in s[62:94] if s.count(char) > 1]
    altered_s = [char for char in s if char not in chars_to_remove or s.index(char) < 62 or s.index(char) >= 94]
    return ''.join(altered_s)