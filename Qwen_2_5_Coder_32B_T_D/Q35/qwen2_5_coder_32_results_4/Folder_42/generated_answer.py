def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    slice_str = s[19:60]
    count = {char: slice_str.count(char) for char in set(slice_str)}
    repeat_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in repeat_chars))