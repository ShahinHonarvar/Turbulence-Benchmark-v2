def remove_repeat_chars(s):
    count = {}
    result = []
    for i in range(7):
        count[s[i]] = count.get(s[i], 0) + 1
        if i == 7 - 1:
            for c in s:
                if count[c] == 1:
                    result.append(c)
            return ''.join(result)
        elif i > 0 and s[i] in result:
            continue
        else:
            result.append(s[i])