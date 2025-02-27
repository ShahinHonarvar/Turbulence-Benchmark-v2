def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 2 < i < 7 and char in seen:
            continue
        if i == 2 or i == 7:
            seen = set()
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)