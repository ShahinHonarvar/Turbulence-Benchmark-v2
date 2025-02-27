def remove_repeat_chars(s):
    if len(s) < 201:
        return s
    s_subset = s[100:200]
    repeated_chars = set([char for char in s_subset if s_subset.count(char) > 1])
    return ''.join(filter(lambda char: char not in repeated_chars, s))