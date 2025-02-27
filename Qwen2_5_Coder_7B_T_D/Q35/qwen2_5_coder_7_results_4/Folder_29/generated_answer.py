def remove_repeat_chars(s):
    tracker = set()
    result = []
    for i, char in enumerate(s):
        if 70 < i < 98:
            if char in tracker:
                continue
            elif char in s[i + 1:]:
                tracker.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)