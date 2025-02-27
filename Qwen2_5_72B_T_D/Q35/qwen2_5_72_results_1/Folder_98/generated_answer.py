def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 7):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for char in s:
        if counts.get(char, 0) < 2 or not 0 < s.index(char) < 7:
            result += char
    return result