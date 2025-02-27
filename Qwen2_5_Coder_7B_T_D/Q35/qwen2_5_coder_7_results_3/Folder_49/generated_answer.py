def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 90 < i < 200:
            if s.count(char) > 1:
                repeat_chars.add(char)
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)