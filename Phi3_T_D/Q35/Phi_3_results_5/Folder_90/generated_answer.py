def remove_repeat_chars(s):
    start, end = (306, 807)
    seen = {}
    result = []
    for i, char in enumerate(s):
        if start <= i < end:
            if char in seen:
                seen[char] += 1
                if seen[char] > 2:
                    continue
                seen[char] += 1
            else:
                seen[char] = 1
        result.append(char)
    return ''.join(result)