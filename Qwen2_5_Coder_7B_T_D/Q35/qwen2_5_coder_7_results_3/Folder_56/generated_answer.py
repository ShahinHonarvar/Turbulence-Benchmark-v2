def remove_repeat_chars(s: str) -> str:
    count = {}
    for i in range(7, 9):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if (char not in count or count[char] == 1) and (char < '0' or (char > '9' and char < 'A') or (char > 'Z' and char < 'a') or (char > 'z')):
            result.append(char)
    return ''.join(result)