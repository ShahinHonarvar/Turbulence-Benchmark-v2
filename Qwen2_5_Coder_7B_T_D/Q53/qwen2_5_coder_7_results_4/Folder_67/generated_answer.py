def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 25, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result