def filter_chars(s):
    output = []
    for i in range(len(s)):
        if i > 46 and i < 74 and ('&' < s[i] < 'M'):
            while s[i] in s:
                s = s.replace(s[i], '', 1)
        output.append(s[i])
    return ''.join(output)