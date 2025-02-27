def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    sub = s[21:35]
    chars_to_remove = {char for char in sub if sub.count(char) > 1}
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)