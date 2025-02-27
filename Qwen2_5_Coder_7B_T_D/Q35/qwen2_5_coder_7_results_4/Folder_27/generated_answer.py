def remove_repeat_chars(s):
    count = {}
    result = ''
    for i, char in enumerate(s):
        if 86 < i < 89:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    for char in s:
        if 86 < s.index(char) < 89 and count[char] > 1 or s.index(char) not in range(86, 89):
            if char not in result:
                result += char
    return result