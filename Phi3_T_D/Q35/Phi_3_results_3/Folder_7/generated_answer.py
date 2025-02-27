def remove_repeat_chars(s):
    target_range = s[375:926]
    seen_chars = set()
    result = []
    for char in target_range:
        if char not in seen_chars:
            seen_chars.add(char)
            result.append(char)
    return s[:375] + ''.join(result) + s[926:]