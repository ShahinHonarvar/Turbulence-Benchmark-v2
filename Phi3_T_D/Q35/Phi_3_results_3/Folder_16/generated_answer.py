def remove_repeat_chars(s):
    char_count = {}
    result = []
    for char in s:
        if 90 < ord(char) < 97:
            if char in char_count:
                char_count[char] += 1
                if char_count[char] > 2:
                    continue
            else:
                char_count[char] = 1
        result.append(char)
    return ''.join(result)