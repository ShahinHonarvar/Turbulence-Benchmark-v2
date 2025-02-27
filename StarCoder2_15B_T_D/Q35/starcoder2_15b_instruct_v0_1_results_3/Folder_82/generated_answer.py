def remove_repeat_chars(string):
    count = {}
    for char in string:
        count[char] = count.get(char, 0) + 1
    result = []
    for char in string:
        if count[char] > 1 and 30 < string.index(char) < 200:
            continue
        result.append(char)
    return ''.join(result)