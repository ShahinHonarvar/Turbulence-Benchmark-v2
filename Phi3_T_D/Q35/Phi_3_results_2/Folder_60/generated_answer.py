def remove_repeat_chars(s):
    indices = range(38, 53)
    to_remove = [char for i, char in enumerate(s) if char in s[i + 1:i + 1 + 25] and i + 1 in indices]
    for char in to_remove:
        s = s.replace(char, '')
    return s