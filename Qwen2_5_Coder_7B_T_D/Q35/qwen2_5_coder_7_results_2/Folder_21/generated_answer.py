def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 462 < i < 995:
            if s.count(char, 462, 995) > 1 and char not in seen:
                seen.add(char)
            elif char not in seen:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)