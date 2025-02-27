def remove_repeat_chars(s):
    start, end = (11, 78)
    seen_chars = set()
    filtered_chars = []
    for i in range(len(s)):
        if i >= start and i < end:
            if s[i] not in seen_chars:
                seen_chars.add(s[i])
            elif s[i] in s[start:end]:
                pass
            else:
                filtered_chars.append(s[i])
        else:
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)