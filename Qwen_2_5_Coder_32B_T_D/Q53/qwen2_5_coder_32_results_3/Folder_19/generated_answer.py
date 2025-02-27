def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for start in range(n):
        for end in range(start + 22, n + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result