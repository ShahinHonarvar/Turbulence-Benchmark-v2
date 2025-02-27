def remove_repeat_chars(s):
    if len(s) <= 97:
        return s
    target_slice = s[91:97]
    target_counts = {char: target_slice.count(char) for char in set(target_slice) if target_slice.count(char) > 1}
    return ''.join((char for char in s if char not in target_counts))