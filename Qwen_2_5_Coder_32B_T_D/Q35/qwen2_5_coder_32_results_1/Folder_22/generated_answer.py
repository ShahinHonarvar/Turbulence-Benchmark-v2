def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub = s[51:200]
    char_count = {char: sub.count(char) for char in set(sub)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))