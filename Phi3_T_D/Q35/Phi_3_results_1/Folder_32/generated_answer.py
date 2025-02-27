def remove_repeat_chars(s):
    count = {}
    unique = []
    idx = 86
    while idx < 90:
        if s[idx] in count and s[idx] not in unique:
            count[s[idx]] -= 1
        else:
            count[s[idx]] = 1
            unique.append(s[idx])
        idx += 1
    return ''.join(unique)