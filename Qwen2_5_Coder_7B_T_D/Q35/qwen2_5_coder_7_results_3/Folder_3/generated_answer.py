def remove_repeat_chars(s):
    counts = {}
    for i in range(57, 88):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in s:
        if counts[char] == 1 or (counts[char] > 1 and 56 < s.index(char) < 88):
            result.append(char)
    return ''.join(result)