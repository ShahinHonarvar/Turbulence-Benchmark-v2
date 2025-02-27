def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 112, n + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result