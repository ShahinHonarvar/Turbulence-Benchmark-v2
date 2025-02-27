def remove_repeat_chars(s):
    counts = {}
    for i in range(376, 926):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join([char for char in s if counts[char] <= 1 or s.index(char) < 375 or s.index(char) >= 926])