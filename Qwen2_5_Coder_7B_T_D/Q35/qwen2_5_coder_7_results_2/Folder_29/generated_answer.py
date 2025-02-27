def remove_repeat_chars(s):
    counts = {}
    for i in range(70, 98):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if char not in counts or (char in counts and counts[char] == 1):
            result.append(char)
    return ''.join(result)