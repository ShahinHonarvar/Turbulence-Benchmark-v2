def remove_repeat_chars(s):
    counts = {}
    for i in range(11, 76):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for char in s:
        if counts[char] <= 1 or char not in s[11:76]:
            result += char
    return result