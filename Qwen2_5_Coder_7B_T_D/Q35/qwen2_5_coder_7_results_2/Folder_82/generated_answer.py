def remove_repeat_chars(s):
    counts = {}
    for i, char in enumerate(s):
        if 30 < i < 200:
            counts[char] = counts.get(char, 0) + 1
    return ''.join((char for char in s if (counts[char] <= 1 or 30 < s.index(char) < 200) and (counts[char] <= 1 or 30 < s.rindex(char) < 200)))