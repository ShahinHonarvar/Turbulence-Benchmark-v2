def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for index, char in enumerate(s):
        if index < 3 and char not in seen_chars and (s.count(char) > 1):
            seen_chars.add(char)
        elif index >= 3 or s.count(char) <= 1:
            result.append(char)
    return ''.join(result)