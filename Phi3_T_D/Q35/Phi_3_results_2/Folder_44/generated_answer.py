def remove_repeat_chars(s):
    target = (36, 52)
    seen = {}
    result = []
    for i, char in enumerate(s):
        if target[0] <= i < target[1]:
            if char in seen:
                if seen[char] == 2:
                    continue
                seen[char] += 1
            else:
                seen[char] = 1
        else:
            result.append(char)
    return ''.join(result)