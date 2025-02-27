def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(70, 200):
        if s[i] in s[70:i]:
            repeat_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)