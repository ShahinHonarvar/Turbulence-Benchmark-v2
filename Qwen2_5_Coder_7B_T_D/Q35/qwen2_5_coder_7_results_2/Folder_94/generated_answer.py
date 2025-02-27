def remove_repeat_chars(s):
    counts = {}
    for i in range(43, 87):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join((char for char in s if (char not in counts or counts[char] == 1) and (s.index(char) < 42 or s.rindex(char) > 87)))