def remove_repeat_chars(s):
    counts = {}
    for char in s[19:32]:
        counts[char] = counts.get(char, 0) + 1
    for char in counts:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s