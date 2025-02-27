def remove_repeat_chars(s):
    repeat_chars = []
    for i in range(40, 43):
        if s[i] in s[39:i] + s[i + 1:]:
            repeat_chars.append(s[i])
    repeat_chars = set(repeat_chars)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)