def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    sub_str = s[47:91]
    char_count = {char: sub_str.count(char) for char in sub_str if sub_str.count(char) > 1}
    return ''.join([char for char in s if char not in char_count])