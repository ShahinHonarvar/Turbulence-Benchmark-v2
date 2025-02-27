def remove_repeat_chars(s):
    count = {}
    for i in range(1, 8):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = []
    for char in s:
        if not (count.get(char, 0) > 1 and 1 <= s.index(char) < 8):
            result.append(char)
    return ''.join(result)