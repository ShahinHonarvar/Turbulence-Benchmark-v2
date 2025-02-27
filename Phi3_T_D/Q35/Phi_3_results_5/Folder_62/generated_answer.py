def remove_repeat_chars(s):
    if len(s) < 43 or len(s) > 141:
        return s
    charset = set()
    start, end = (50, 93)
    result = []
    for i in range(len(s)):
        if start <= i < end:
            if s[i] in charset:
                continue
            if s.count(s[i], start, end) > 1:
                charset.add(s[i])
            else:
                result.append(s[i])
        else:
            result.append(s[i])
    return ''.join(result)