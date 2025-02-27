def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 73 < i < 84:
            if char in repeat_chars:
                continue
            if s.count(char, 73, 84) > 1:
                repeat_chars.add(char)
        result.append(char)
    return ''.join(result)