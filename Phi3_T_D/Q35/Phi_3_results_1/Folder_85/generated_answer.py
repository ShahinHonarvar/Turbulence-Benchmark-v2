def remove_repeat_chars(s):
    seen_chars = set()
    altered_string = []
    for i, char in enumerate(s[1:8]):
        if char not in seen_chars:
            seen_chars.add(char)
            altered_string.append(char)
    return s[0] + ''.join(altered_string) + s[8:]