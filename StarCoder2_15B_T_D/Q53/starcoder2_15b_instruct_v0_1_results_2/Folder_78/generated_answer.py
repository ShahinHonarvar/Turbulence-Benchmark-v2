import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pattern = '[a-z]'
    matches = re.findall(pattern, string)
    matches = ''.join(matches)
    n = 96
    result = []
    for i in range(len(matches) - n + 1):
        s = matches[i:i + n]
        if s == s[::-1]:
            result.append(s)
    return set(result)