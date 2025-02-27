def remove_repeat_chars(s):
    seen = set()
    result = []
    for index, char in enumerate(s):
        if 69 < index < 97:
            if char in seen:
                continue
            seen.add(char)
        result.append(char)
    return ''.join(result)