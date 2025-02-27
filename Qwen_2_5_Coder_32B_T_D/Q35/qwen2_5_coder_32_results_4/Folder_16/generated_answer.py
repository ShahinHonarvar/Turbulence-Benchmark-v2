def remove_repeat_chars(s):
    if len(s) <= 98:
        return s
    check_area = s[91:97]
    chars_to_remove = {char for char in check_area if check_area.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))