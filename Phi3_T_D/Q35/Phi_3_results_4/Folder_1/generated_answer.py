def remove_repeat_chars(s):
    unique_chars = []
    for i in range(17, 88):
        char = s[i]
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join((char for char in s if char in unique_chars))