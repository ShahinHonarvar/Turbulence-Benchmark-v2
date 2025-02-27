def remove_repeat_chars(s):
    if len(s) <= 202:
        return s
    check_range = s[201:202]
    count = {char: s.count(char) for char in set(check_range)}
    chars_to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in chars_to_remove))