def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 80 < i < 200:
            if s.count(char, 80, 200) > 1:
                if char not in seen:
                    seen.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)