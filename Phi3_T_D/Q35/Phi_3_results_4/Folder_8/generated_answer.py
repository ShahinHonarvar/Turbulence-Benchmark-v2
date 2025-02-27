def remove_repeat_chars(s):
    repeated_chars = set(s[45:48])
    result = [char for char in s if char not in repeated_chars or s[45:48].count(char) == 1]
    return ''.join(result)