def remove_repeat_chars(s):
    if len(s) <= 65:
        return s
    check_range = s[36:64]
    remove_chars = {char for char in check_range if check_range.count(char) > 1}
    return ''.join((char for char in s if char not in remove_chars))