def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(len(s)):
        if 6 < i < 9:
            if s[i] not in seen:
                seen.add(s[i])
                result.append(s[i])
        else:
            result.append(s[i])
    return ''.join(result)