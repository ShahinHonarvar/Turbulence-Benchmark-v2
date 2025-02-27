def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 9):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''.join([char for char in s if counts.get(char, 0) <= 1 or s.index(char) not in range(1, 9)])
    return result