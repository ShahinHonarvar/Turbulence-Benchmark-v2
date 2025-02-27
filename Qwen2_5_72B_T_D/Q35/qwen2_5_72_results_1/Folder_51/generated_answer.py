def remove_repeat_chars(s):
    counts = {}
    for i in range(6, 10):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for char in s:
        if counts.get(char, 0) < 2 or 6 <= s.index(char) <= 9:
            result += char
    return result