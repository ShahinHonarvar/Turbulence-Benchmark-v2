def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 5):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = [char for char in s if char not in counts or counts[char] < 2]
    return ''.join(result)