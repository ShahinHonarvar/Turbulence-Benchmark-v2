def remove_repeat_chars(s):
    if len(s) <= 92:
        return s
    segment = s[14:91]
    char_count = {char: segment.count(char) for char in set(segment)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))