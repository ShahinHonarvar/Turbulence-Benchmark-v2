def remove_repeat_chars(s):
    specific_part = s[10:76]
    seen_chars = set()
    result_chars = []
    for char in specific_part:
        if char in seen_chars:
            continue
        if specific_part.count(char) > 1:
            seen_chars.add(char)
            continue
        result_chars.append(char)
    offset = len(s) - len(specific_part)
    return s[:10] + ''.join(result_chars) + s[76:]