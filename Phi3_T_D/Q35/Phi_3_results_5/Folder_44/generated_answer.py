def remove_repeat_chars(s):
    chars_to_remove = [char.lower() for char in set(s[36:52].lower()) if s[36:52].lower().count(char) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
        s = s.replace(char.upper(), '')
    return s