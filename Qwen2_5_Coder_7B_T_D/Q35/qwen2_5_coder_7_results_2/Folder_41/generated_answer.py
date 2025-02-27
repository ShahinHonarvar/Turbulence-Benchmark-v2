def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 3 < i < 8 and s.count(char) > 1:
            repeat_chars.add(char)
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)