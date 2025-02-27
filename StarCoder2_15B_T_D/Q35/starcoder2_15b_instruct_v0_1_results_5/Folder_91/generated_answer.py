def remove_repeat_chars(s):
    substring = s[1:5]
    unique_chars = {c for c in substring}
    new_chars = [c for c in s if c not in unique_chars]
    new_string = ''.join(new_chars)
    return new_string