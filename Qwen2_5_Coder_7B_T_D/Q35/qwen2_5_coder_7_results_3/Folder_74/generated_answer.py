def remove_repeat_chars(s):
    count = {}
    result = []
    for i, char in enumerate(s):
        if 69 < i < 97:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    for char in s:
        if count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)