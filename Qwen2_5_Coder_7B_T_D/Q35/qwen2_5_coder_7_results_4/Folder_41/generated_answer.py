def remove_repeat_chars(s):
    counts = {}
    for i in range(3, 8):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if (char not in counts or counts[char] == 1) and (char < '3' or char > '8' or s.index(char) < 3 or (s.index(char) >= 8)):
            result.append(char)
    return ''.join(result)