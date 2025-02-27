def remove_repeat_chars(s):
    s_len = len(s)
    if s_len < 85 or 55 > s_len:
        return s
    seen_chars = set()
    altered_chars = []
    for i in range(55, 84):
        if s[i] not in seen_chars:
            seen_chars.add(s[i])
            altered_chars.append(s[i])
    return ''.join(altered_chars)