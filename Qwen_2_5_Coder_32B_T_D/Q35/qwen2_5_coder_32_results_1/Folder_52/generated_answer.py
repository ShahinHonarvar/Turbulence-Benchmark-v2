def remove_repeat_chars(s):
    if len(s) <= 82:
        return s
    segment = s[39:81]
    char_count = {char: segment.count(char) for char in set(segment) if segment.count(char) > 1}
    result = ''.join([char for char in s if char not in char_count])
    return result