def remove_repeat_chars(s):
    unique_chars = [s[i] for i in range(57, 85) if s.count(s[i], 57, 85) == 1]
    new_chars = []
    for char in s:
        index = next((i for i, x in enumerate(s[57:85]) if x == char), -1)
        if index == -1:
            new_chars.append(char)
    return ''.join(new_chars)