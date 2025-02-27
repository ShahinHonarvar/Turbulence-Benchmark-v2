def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(20, 35):
        if s[i] in s[20:i] or s[i] in s[i + 1:35]:
            repeat_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)