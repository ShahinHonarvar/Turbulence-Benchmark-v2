def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i > 4:
            break
        if char in s[i + 1:]:
            seen.add(char)
        elif char not in seen:
            result.append(char)
    return ''.join(result)