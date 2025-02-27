def remove_repeat_chars(s):
    if len(s) < 150:
        return s
    seen_chars = set()
    placed_chars = []
    for idx, char in enumerate(s[50:200]):
        if char not in seen_chars:
            placed_chars.append((idx + 50, char))
            seen_chars.add(char)
    new_s = ''
    last_idx = 0
    for idx, char in placed_chars:
        new_s += s[last_idx:idx]
        last_idx = idx + 1
    new_s += s[last_idx:]
    return new_s