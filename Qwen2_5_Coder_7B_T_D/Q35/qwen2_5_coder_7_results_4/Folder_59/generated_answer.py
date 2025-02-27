def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(1, 10):
        char = s[i]
        if char in s[:i] and char in s[i + 1:]:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)