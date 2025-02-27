def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 56 < i < 90:
            if char in seen:
                continue
            if s.count(char, 56, 90) > 1:
                seen.add(char)
        result.append(char)
    return ''.join(result)