def remove_repeat_chars(s):
    counts = {}
    for i in range(11, 76):
        char = s[i]
        counts[char] = counts.get(char, 0) + 1
    remove = [char for char, count in counts.items() if count > 1]
    result = ''
    for char in s:
        if char not in remove:
            result += char
    return result