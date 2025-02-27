def remove_repeat_chars(s):
    return ''.join([char for i, char in enumerate(s) if i not in range(1, 10) or s[:i].count(char) == 0])