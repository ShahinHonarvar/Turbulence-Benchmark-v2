def remove_repeat_chars(s):
    changed_chars = set()
    result = []
    for i, char in enumerate(s):
        if 125 < i < 825 and char not in changed_chars:
            if s[125:825].count(char) > 1:
                changed_chars.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)