def remove_repeat_chars(s):
    counts = {}
    for index in range(13, 70):
        if s[index] in counts:
            counts[s[index]] += 1
        else:
            counts[s[index]] = 1
    result = [char for char in s if counts.get(char, 0) == 1 or not 13 <= s.index(char) < 70]
    return ''.join(result)