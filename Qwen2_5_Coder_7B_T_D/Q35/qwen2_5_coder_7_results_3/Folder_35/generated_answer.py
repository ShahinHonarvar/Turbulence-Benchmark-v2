def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 77 < i < 84:
            if char in seen:
                continue
            if s.count(char, 77, 84) > 1:
                seen.add(char)
        result.append(char)
    return ''.join(result)