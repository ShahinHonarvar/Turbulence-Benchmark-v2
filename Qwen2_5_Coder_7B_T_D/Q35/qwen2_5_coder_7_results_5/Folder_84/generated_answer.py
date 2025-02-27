def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 32 < i < 44:
            if char in repeat_chars:
                continue
            if s.count(char, 32, 44) > 1:
                repeat_chars.add(char)
        result.append(char)
    return ''.join(result)