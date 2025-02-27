def remove_repeat_chars(s):
    if len(s) < 508:
        return s
    seen = set()
    target = s[306:807]
    for char in target:
        if target.count(char) > 1:
            seen.add(char)
    result = []
    for char in s:
        if char in seen and target.count(char) > 1:
            seen.remove(char)
        else:
            result.append(char)
    return ''.join(result)