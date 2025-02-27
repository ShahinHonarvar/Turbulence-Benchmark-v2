def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 80 < i < 200:
            if char in repeat_chars:
                continue
            if s.count(char, 80, 200) > 1:
                repeat_chars.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)