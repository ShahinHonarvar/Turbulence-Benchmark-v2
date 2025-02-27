def remove_repeat_chars(s):
    start, end = (22, 25)
    char_count = {char: 0 for char in s[start:end]}
    for char in char_count:
        char_count[char] = s.count(char)
    return ''.join([char for char in s if not (start < s.index(char) < end and char_count[char[start:end]] > 1)])