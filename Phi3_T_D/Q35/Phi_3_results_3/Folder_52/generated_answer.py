def remove_repeat_chars(s):
    seen = {}
    for i in range(38, 81):
        if s[i] in seen:
            seen[s[i]] += 1
        else:
            seen[s[i]] = 1
    for char, count in seen.items():
        if count > 1 and char in s[38:81]:
            s = s.replace(char, '')
    return s