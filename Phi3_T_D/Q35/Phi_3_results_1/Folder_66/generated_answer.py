def remove_repeat_chars(s):
    unique_chars = []
    for i in range(11, 76):
        if s[i] not in unique_chars:
            unique_chars.append(s[i])
    return ''.join([c for c in s if c in unique_chars or not 11 <= i <= 76])