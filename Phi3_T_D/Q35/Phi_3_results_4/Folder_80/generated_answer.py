def remove_repeat_chars(s):
    unique_chars = []
    for char in s[57:83]:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)