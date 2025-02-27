def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 69 < i < 97:
            if char in repeat_chars:
                continue
            if s.count(char, 69, 97) > 1:
                repeat_chars.add(char)
        result.append(char)
    return ''.join(result)