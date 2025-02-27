def remove_repeat_chars(s):
    counts = {}
    for i in range(60, 200):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join([char for i, char in enumerate(s) if i < 60 or i >= 200 or counts[char] == 1])