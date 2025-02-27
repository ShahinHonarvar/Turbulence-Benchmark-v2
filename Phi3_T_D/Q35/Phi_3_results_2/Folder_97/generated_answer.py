def remove_repeat_chars(s):
    if len(s) <= 34 or len(s) >= 69:
        return s
    start, end = (34 + 1, 68)
    char_positions = {}
    for i in range(start, end):
        char = s[i]
        if char in char_positions:
            char_positions[char].append(i)
        else:
            char_positions[char] = [i]
    result_chars = []
    seen_chars = set()
    for i in range(len(s)):
        if i < start or i >= end or s[i] not in seen_chars:
            result_chars.append(s[i])
            seen_chars.add(s[i])
    return ''.join(result_chars)