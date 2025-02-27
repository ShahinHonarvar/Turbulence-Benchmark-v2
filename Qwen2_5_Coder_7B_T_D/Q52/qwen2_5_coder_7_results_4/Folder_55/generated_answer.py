def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n - 96):
        substring = s[i:i + 97]
        if substring == substring[::-1]:
            result.add(substring)
    return result