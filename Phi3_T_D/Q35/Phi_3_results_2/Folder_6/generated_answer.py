def remove_repeat_chars(s):
    sub_str = s[20:93]
    seen = set()
    altered_chars = []
    for char in sub_str:
        if char in seen:
            continue
        if sub_str.count(char) > 1:
            sub_str = sub_str.replace(char, '')
        else:
            altered_chars.append(char)
            seen.add(char)
    return s[:20] + ''.join(altered_chars) + s[93:]