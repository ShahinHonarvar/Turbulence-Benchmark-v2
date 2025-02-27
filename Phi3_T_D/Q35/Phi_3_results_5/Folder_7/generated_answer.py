def remove_repeat_chars(s):
    start, end = (375, 926)
    unique_chars = set()
    result = []
    for i, char in enumerate(s[start:end]):
        if char in unique_chars:
            continue
        if s[start:end].count(char) > 1:
            s = s[:start + i] + s[start + i + 1:end]
            i -= 1
        result.append(char)
        unique_chars.add(char)
    return ''.join(result)