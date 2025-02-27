def remove_repeat_chars(s):
    counts = {}
    for i in range(39, 43):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = [char for char in s if counts.get(char, 0) <= 1]
    return ''.join(result)