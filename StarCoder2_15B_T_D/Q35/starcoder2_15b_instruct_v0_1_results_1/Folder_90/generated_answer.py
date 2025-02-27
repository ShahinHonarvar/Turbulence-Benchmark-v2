def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for c in s[306:807]:
        char_count[c] = char_count.get(c, 0) + 1
    repeated_chars = {c for c, count in char_count.items() if count > 1}
    result = []
    for c in s:
        if c not in repeated_chars:
            result.append(c)
    return ''.join(result)