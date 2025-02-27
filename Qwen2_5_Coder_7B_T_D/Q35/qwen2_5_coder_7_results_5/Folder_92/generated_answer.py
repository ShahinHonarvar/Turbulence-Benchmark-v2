def remove_repeat_chars(s):
    count = {}
    for i in range(1, 3):
        count[s[i]] = count.get(s[i], 0) + 1
    result = [s[0]]
    for char in s[1:]:
        if count[char] == 0:
            result.append(char)
    return ''.join(result)