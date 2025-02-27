def remove_repeat_chars(s):
    seen = {}
    new_s = []
    for i, char in enumerate(s):
        if i < 2:
            continue
        if char in seen:
            if seen[char] < 2:
                seen[char] += 1
            else:
                continue
        else:
            seen[char] = 1
        new_s.append(char)
    return ''.join(new_s)