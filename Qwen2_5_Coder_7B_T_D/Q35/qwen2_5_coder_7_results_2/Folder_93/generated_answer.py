def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i in range(57, 85):
        if s[i] in s[:57] + s[85:]:
            repeat_chars.add(s[i])
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)