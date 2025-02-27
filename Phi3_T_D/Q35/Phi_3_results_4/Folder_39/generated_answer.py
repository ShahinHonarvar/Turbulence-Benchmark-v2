def remove_repeat_chars(s):
    seen_chars = set()
    altered_s = []
    for i in range(44, 91):
        if s[i] in seen_chars:
            continue
        seen_chars.add(s[i])
        altered_s.append(s[i])
    return ''.join(altered_s)