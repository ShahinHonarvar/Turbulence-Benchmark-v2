def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for i, char in enumerate(s):
        if i >= 3 and i <= 9:
            if char in unique_chars:
                continue
            if s.count(char, i) > 1:
                unique_chars.add(char)
            else:
                result.append(char)
        elif i < 3 or i > 9:
            result.append(char)
    return ''.join(result)