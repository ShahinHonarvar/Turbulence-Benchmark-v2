def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 147
    result = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= n:
                result.add(substring)
    return result