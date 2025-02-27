def remove_repeat_chars(string):
    chars = set()
    result = []
    for char in string:
        if string.count(char) > 1 and 2 < string.index(char) < 5:
            if char not in chars:
                chars.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)