def remove_repeat_chars(s):
    counts = {}
    result = []
    for i, char in enumerate(s):
        if 40 < i < 200:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
            if counts[char] == 2:
                result.append(char)
    return ''.join([char for char in s if char not in result])