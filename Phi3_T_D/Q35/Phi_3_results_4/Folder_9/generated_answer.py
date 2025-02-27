def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    start = 80
    end = 200
    if start >= end or end > len(s):
        return s
    char_counts = {}
    for i in range(start, end):
        char = s[i]
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    result = []
    for i in range(len(s)):
        if char_counts.get(s[i], 1) == 1 or i < start or i >= end:
            result.append(s[i])
    return ''.join(result)