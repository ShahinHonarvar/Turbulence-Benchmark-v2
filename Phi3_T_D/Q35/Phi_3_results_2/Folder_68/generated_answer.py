def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(10, len(s)):
        if s[i] not in seen:
            if s[i] not in s[:10]:
                seen.add(s[i])
                result.append(s[i])
    return ''.join(result)