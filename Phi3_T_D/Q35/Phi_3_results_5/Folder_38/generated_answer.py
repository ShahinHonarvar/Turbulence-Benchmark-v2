def remove_repeat_chars(s):
    chars = set()
    result = []
    for i, char in enumerate(s):
        if 36 < i < 85 and char in chars:
            continue
        if 36 < i < 85:
            chars.add(char)
        result.append(char)
    return ''.join(result)