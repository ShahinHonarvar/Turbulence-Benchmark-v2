def remove_repeat_chars(s):
    if len(s) <= 90:
        return s
    check_range = s[57:90]
    char_count = {char: check_range.count(char) for char in set(check_range)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))