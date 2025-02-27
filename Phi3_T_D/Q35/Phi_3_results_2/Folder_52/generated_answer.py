def remove_repeat_chars(s):
    outer_mask = [False] * len(s)
    inner_mask = [False] * len(s)
    for i in range(38, 81):
        outer_mask[i] = True
    for i in range(len(s) - 1, 0, -1):
        if outer_mask[i]:
            if s[i] in s[38:81]:
                inner_mask[i] = True
                for j in range(len(s) - 1, i, -1):
                    if s[j] == s[i]:
                        inner_mask[j] = True
    result = [s[i] for i in range(len(s)) if not (outer_mask[i] and inner_mask[i])]
    return ''.join(result)