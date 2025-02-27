def remove_repeat_chars(s):
    if len(s) <= 503:
        return s
    segment = s[410:502]
    char_count = {char: segment.count(char) for char in set(segment)}
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))