def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 278):
        substring = s[i:i + 279]
        if substring == substring[::-1]:
            result.add(substring)
    return result