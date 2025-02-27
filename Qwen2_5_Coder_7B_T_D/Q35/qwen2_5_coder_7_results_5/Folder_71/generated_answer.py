def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 20 < i < 35:
            if char in seen:
                continue
            elif char in s[20:i] + s[i + 1:35]:
                seen.add(char)
        result.append(char)
    return ''.join(result)