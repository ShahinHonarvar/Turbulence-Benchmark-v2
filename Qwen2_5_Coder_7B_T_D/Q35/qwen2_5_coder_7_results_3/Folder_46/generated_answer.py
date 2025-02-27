def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 10 < i < 79:
            if s.count(char) > 1:
                if char not in seen:
                    seen.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)