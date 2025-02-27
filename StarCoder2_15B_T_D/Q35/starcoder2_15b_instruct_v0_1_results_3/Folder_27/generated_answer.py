def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 0
        char_count[c] += 1
    repeated_chars = [c for c in char_count if char_count[c] > 1 and 86 < ord(c) < 89]
    for c in repeated_chars:
        s = s.replace(c, '')
    return s