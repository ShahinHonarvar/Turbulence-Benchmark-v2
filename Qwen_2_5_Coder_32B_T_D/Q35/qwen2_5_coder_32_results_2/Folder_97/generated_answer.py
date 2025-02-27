def remove_repeat_chars(s):
    if len(s) <= 69:
        return s
    target_segment = s[35:69]
    repeats = {char for char in target_segment if target_segment.count(char) > 1}
    return ''.join((char for char in s if char not in repeats))