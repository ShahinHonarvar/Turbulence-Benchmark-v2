def remove_repeat_chars(s):
    seen_chars = set()
    result_chars = []
    for i in range(30, 200):
        char = s[i]
        if char not in seen_chars:
            seen_chars.add(char)
            result_chars.append(char)
    return ''.join(result_chars)