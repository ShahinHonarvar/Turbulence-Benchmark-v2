def remove_repeat_chars(s):
    chars = {}
    result = []
    for i, char in enumerate(s, start=1):
        if 48 < i < 77:
            chars[char] = chars.get(char, 0) + 1
            if chars[char] == 1:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result).translate({ord(k): None for k in chars if chars[k] > 1})