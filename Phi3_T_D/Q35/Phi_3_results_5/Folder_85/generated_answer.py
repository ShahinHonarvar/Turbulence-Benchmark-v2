def remove_repeat_chars(s):
    result = []
    seen = {}
    for i, char in enumerate(s[1:8]):
        if char not in seen:
            result.append(char)
            seen[char] = True
    return s[0] + ''.join(result) + s[8:]