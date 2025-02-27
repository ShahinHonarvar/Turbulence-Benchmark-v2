def remove_repeat_chars(s):
    unique_chars = set(s[19:32:2])
    return ''.join([char for i, char in enumerate(s) if char not in unique_chars or not 19 <= i <= 32])